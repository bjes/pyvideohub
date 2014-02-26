import colander
import deform
from deform.schema import FileData
from deform.widget import FileUploadWidget

class _TmpStore(dict):
    def preview_url(self, name):
        return None

class UploadSchema(colander.MappingSchema):
    title = colander.SchemaNode(colander.String(),
        validator=colander.Length(max=100),
        widget=deform.widget.TextInputWidget())
    description = colander.SchemaNode(colander.String(),
        validator=colander.Length(max=250),
        widget=deform.widget.TextAreaWidget(rows=10))
    file = colander.SchemaNode(FileData(), widget=FileUploadWidget(_TmpStore()))
