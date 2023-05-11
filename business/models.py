from django.db import models

class Business (models.Model):
    SHIRT_SIZES = [
                ("ديكور", "اعمال الديكور"),
                ("أخرى", "اعمال أخرى"),
                ("السباكة", "السباكة"),
                ("الكهربائيات", "الكهربائيات"),
                  ]
    name=models.CharField(max_length=200)
    type=models.CharField( max_length=100,choices=SHIRT_SIZES)
    
    
    def __str__(self):
        return self.name
    