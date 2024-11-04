from django.db import models
from django.urls import reverse 
from django import forms # new
from accounts.models import CustomUser

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    #author = models.ForeignKey(
    #    'auth.User',
    #    on_delete=models.CASCADE,
    #)
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): #new
        return reverse("post_detail", kwargs={"pk": self.pk}) # new
    
# ModelForm 
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body']  # Include all fields in the form
        labels = {
            'title': 'Post Title',  # Custom label for title field
            'author': 'Author Name',  # Custom label for author field
            'body': 'Post Content',  # Custom label for body field
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',  # Bootstrap class for styling
                'placeholder': 'Enter a descriptive title for your post'  # Placeholder text
            }),
            'author': forms.Select(attrs={
                'class': 'form-control',  # Bootstrap class for dropdown
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',  # Bootstrap class for styling textarea
                'rows': 5,  # Set height of the textarea
                'placeholder': 'Write the content of your post here'  # Placeholder for body
            }),
        }
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        #Set the queryset for the author field
        self.fields['author'].queryset = CustomUser.objects.all()