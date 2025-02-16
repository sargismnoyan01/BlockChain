from .models import Block


def get_last_block():
    return Block.objects.last()


def create_new_block(data):
    last_block = get_last_block()
    index = last_block.index + 1 if last_block else 0
    previous_hash = last_block.hash if last_block else "0"

    new_block = Block(index=index, previous_hash=previous_hash, data=data)
    new_block.save()
    return new_block
