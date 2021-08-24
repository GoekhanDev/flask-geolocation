from datetime import date
from app import *

class update():

    def __init__(self):

        self.Files = []

        if not os.path.exists("./data"):
            
            if not os.path.exists("./apikey.txt"):
                    
                    while True:
                        
                        apiKey = input("""\rYou currently don't have a MaxMind license key configured
                            \rPlease visit the following address to obtain a free or paid key:
                            \rhttps://www.maxmind.com/en/my_license_key
                            \rMaxMind License Key: """)
                        
                        if len(apiKey) == 16:
                            open("./apikey.txt", "w+").write(apiKey)
                            break
                        
                        else: 
                            print("invailid apikey, please try again...")
                            time.sleep(2)
                            continue
            
            os.mkdir("./data")

        else: 

            if os.path.exists("./lastUpdated.txt"):
                if ((datetime.datetime.now() - datetime.datetime.strptime(
                    open("./lastUpdated.txt", "r").read(), "%Y-%m-%d %H:%M:%S.%f")).days == 3):
                    shutil.rmtree("data")

        self.apiKey = str(open("./apikey.txt", "r").read()).strip()

        for edition in ["City"]:
            if not os.path.exists(f"./data/GeoLite2-{edition}.mmdb"):
                self.Files.append(edition)

        if self.Files != []:
            
            for file in self.Files:
                t = threading.Thread(target=self.download, args=[file])
                t.start()

            t.join()

            while self.Files != []:
                time.sleep(1)

        while not os.path.exists("./data/lastUpdated.txt"):
            os.system('cls' if os.name=='nt' else 'clear')
            open("./data/lastUpdated.txt", "w+").write(str(datetime.datetime.now()))

    def download(self, edition):

        print(f"downloading: GeoLite2-{edition}.tar.gz")

        response = requests.get("https://download.maxmind.com/app/geoip_download", 
            params={"edition_id": f"GeoLite2-{edition}", "license_key": self.apiKey, "suffix": "tar.gz"}, stream=True)

        with open(f"./data/{edition}.tar.gz", "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)

        print(f"extracting: GeoLite2-{edition}.tar.gz")

        file = tarfile.open(f'./data/{edition}.tar.gz'); file.extractall('./data/'); file.close()

        for folder in [folder for folder in glob.glob("./data/*") if "GeoLite2" in folder and "_2" in folder]:
            file_names = os.listdir(folder)
            for file_name in file_names:
                if ".txt" not in file_name:
                    try: shutil.move(os.path.join(folder, file_name), "./data/")
                    except: pass
            shutil.rmtree(folder)

        print(f"done: GeoLite2-{edition}.tar.gz")

        os.remove(f"./data/{edition}.tar.gz"); self.Files.remove(edition)

update()