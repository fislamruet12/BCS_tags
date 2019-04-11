from django.db import models

# Create your models here.

class subjects(models.Model):
    name=models.CharField(max_length=100)
    bio=models.CharField(max_length=100)
    model_pic = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

    def __str__(self):
      return  self.name

class subcatagory(models.Model):
    subject_id=models.ForeignKey(subjects,on_delete=models.CASCADE)
    catalist=models.CharField(max_length=100)

    def __str__(self):
        return self.catalist



class contcatagory(models.Model):
    subcatagory_id=models.ForeignKey(subcatagory,on_delete=models.CASCADE)
    contentlist=models.CharField(max_length=100)
    cata_pic = models.ImageField(upload_to='cata_folder/', default='cata_folder/None/no-img.jpg')

    def __str__(self):
        return self.contentlist

    @property
    def contents(self):
        return self.contentelement_set.all()


# catagory wise models


class contentelement(models.Model):
    contcatagory_id=models.ForeignKey(contcatagory,on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=45000)
    date = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return self.title
    @property
    def images(self):
        return self.contentelementimage_set.all()

    @property
    def contenttable(self):
        return self.contenttabletitle_set.all()

    @property
    def qutypes(self):
        return self.types_set.all()


class contentelementimage(models.Model):
    contentelement_id = models.ForeignKey(contentelement, on_delete=models.CASCADE)
    content_pic = models.ImageField(upload_to='content_folder/', default='content_folder/None/no-img.jpg')
    title=models.CharField(max_length=100,null=True)

class contenttabletitle(models.Model):
     contenttable_id=models.ForeignKey(contentelement,on_delete=models.CASCADE)
     title=models.CharField(max_length=250)
     cl1 = models.CharField(max_length=50,null=True)
     cl2 = models.CharField(max_length=50,null=True)
     cl3 = models.CharField(max_length=50,null=True)
     cl4 = models.CharField(max_length=50,null=True)
     cl5 = models.CharField(max_length=50,null=True)
     cl6 = models.CharField(max_length=50,null=True)

     def __str__(self):
         return self.title

     @property
     def tableinfo(self):
         return self.contenttableinfo_set.all()

class contenttableinfo(models.Model):
    contenttabletitle_id = models.ForeignKey(contenttabletitle, on_delete=models.CASCADE)
    tl1 = models.CharField(max_length=450,null=True)
    tl2 = models.CharField(max_length=450,null=True)
    tl3 = models.CharField(max_length=450,null=True)
    tl4 = models.CharField(max_length=450,null=True)
    tl5 = models.CharField(max_length=450,null=True)
    tl6 = models.CharField(max_length=450,null=True)


class types(models.Model):
    types_id=models.ForeignKey(contentelement,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
    def allquestion(self):
        return self.question_set.all()

class question(models.Model):
    question_id=models.ForeignKey(types,on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    que_pic = models.ImageField(upload_to='que_folder/', default='que_folder/None/no-img.jpg')
    op1 = models.CharField(max_length=200)
    op2 = models.CharField(max_length=200)
    op3 = models.CharField(max_length=200)
    op4 = models.CharField(max_length=200)
    ans = models.IntegerField()
    explain = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.question_id)
