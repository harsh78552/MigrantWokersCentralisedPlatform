Allowed_Extensions = ['pdf', 'jpeg', 'jpg', 'png']


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Allowed_Extensions
