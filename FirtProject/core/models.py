import hashlib
import datetime
from django.db import models

class Block(models.Model):
    index = models.IntegerField(unique=True)
    previous_hash = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.TextField()
    transaction_hash = models.CharField(max_length=66, null=True, blank=True)  # Hash of the transaction
    hash = models.CharField(max_length=64, unique=True)

    def save(self, *args, **kwargs):
        if not self.hash:
            self.hash = self.calculate_hash()
        if not self.previous_hash:
            last_block = Block.objects.order_by('-index').first()
            self.previous_hash = last_block.hash if last_block else '0' * 64
        super().save(*args, **kwargs)

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(f"{self.index}{self.previous_hash}{self.timestamp}{self.data}".encode('utf-8'))
        return sha.hexdigest()


