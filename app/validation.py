from app import *

def validation(reqargs):
    
    ip, errors = reqargs.get("ip"), []

    if not ip:
        errors.append("ip value is required")

    try: ipaddress.ip_address(ip)
    except ValueError: errors.append("Invailid ip address")

    if errors != []: 
        return jsonify({'Error': {'message': [', '.join(elem for elem in errors)]} }), 400

    return True
