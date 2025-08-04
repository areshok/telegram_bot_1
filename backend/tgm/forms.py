from django import forms

from .models import CommentProduct, MarketingMessage


class CommentProductFormUser(forms.ModelForm):
    status_boolean = forms.BooleanField(required=False)

    class Meta:
        model = CommentProduct
        fields = ["product_id", "comment", "score", "status_boolean"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.status == CommentProduct.Status.VIEWED:
            self.fields["status_boolean"].initial = True

        self.fields["product_id"].disabled = True
        self.fields["comment"].disabled = True
        self.fields["score"].disabled = True


class MarketingMessageForm(forms.ModelForm):

    class Meta:
        model = MarketingMessage
        fields = ["product_id", "title", "body", "image"]
