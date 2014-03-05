from wtforms import Form, StringField, TextAreaField, FileField, validators

class UploadForm(Form):
    title = StringField('影片標題',
        [validators.InputRequired(message='影片標題為必要欄位'),
         validators.Length(max=100, message='文字長度限制在 100 字以下')])
    description = TextAreaField('影片說明',
        [validators.Length(max=65535, message='文字長度限制在 65535 字以下')])
    file = FileField('影片檔案')

    def validate_file(form, field):
        from cgi import FieldStorage
        if not isinstance(field.data, FieldStorage):
            raise validators.ValidationError('影片檔案為必要欄位')
