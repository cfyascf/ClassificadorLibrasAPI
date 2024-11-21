from marshmallow import Schema, fields

from app.errors.app import AppError

class ClassificationSchema(Schema):
    model_type = fields.Str(required=True)
    file = fields.Raw(required=True)

    @staticmethod
    def validate(request):
        schema = ClassificationSchema()
        form_data = request.form.to_dict()

        if 'media' not in request.files:
            raise AppError(403, "Media file is mandatory.")
            
        file = request.files['media']
        if file.filename == '':
            raise AppError(403, "Media file is mandatory.")
        
        # ..checks if the file exists and 
        # integrates it to the form..
        form_data['file'] = file
        data = schema.load(form_data)

        return data
