# from services.getprice import save_xls

def lambda_handler(event, context):
    message = event.get('tienda')
    return {
        'message': message
    }
