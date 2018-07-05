from django import forms


class UploadImageForm(forms.Form):
    image = forms.FileField()

    def clean_image(self):
        image = self.cleaned_data['image']
        # TODO: add image size limit and file type checking
        return image
