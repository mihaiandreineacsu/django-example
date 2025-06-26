# ✅ Migrating an Existing M2M Field to a through= Model (Without Losing Data)

This guide walks you through converting an existing `ManyToManyField` into one that uses a `through=` model—**without losing existing relations**.

---

## 🧩 Starting Situation

You originally had:

```python
class Post(models.Model):
    category = models.ForeignKey(Category, ...)
```

Then you switched to:

```python
class Post(models.Model):
    categories = models.ManyToManyField(to=Category, related_name="posts")
```

This generated a migration like:

```python
migrations.RemoveField(model_name="post", name="category"),
migrations.AddField(model_name="post", name="categories", field=models.ManyToManyField(to="core.category", related_name="posts")),
```

You may have even added some relations via the Django admin at this point.

---

## 🔄 Now You Want to Use **through=PostCategory**

```python
class Post(models.Model):
    categories = models.ManyToManyField(to=Category, through="core.PostCategory")

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
```

But when you try to **alter the existing** `ManyToManyField` to use `through=PostCategory`, you’ll get this error:

```bash
ValueError: Cannot alter field ... they are not compatible types (you cannot alter to or from M2M fields, or add or remove through= on M2M fields)
```

---

## ✅ Solution: Safe Migration Plan

1. **Rollback the Breaking Migration**

If you already tried the `through=` change and hit an error, first delete the failed migration file and revert the model to use a standard M2M (without `through=`).

1. **Create the `PostCategory` Model**

Add this model:

```python
class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
```

Create and run the migration:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

1. **Add a Temporary M2M With `through=`**

Temporarily add a second field using `through=PostCategory`:

```python
class Post(models.Model):
    categories = models.ManyToManyField(to=Category, related_name="posts")
    categories_through = models.ManyToManyField(to=Category, through="core.PostCategory")
```

Make and run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

1. **Migrate Existing Data**

Create an empty migration:

```bash
python manage.py makemigrations core --empty --name migrate_categories_to_through
```

Update it like this:

```python
import datetime
from django.db import migrations

def forward(apps, schema_editor):
    Post = apps.get_model("core", "Post")
    PostCategory = apps.get_model("core", "PostCategory")
    for post in Post.objects.all():
        for category in post.categories.all():
            PostCategory.objects.get_or_create(
                post=post,
                category=category,
                defaults={"date_created": datetime.date.today()},
            )

class Migration(migrations.Migration):
    dependencies = [
        ("core", "XXXX_previous_migration"),
    ]

    operations = [
        migrations.RunPython(forward, reverse_code=migrations.RunPython.noop),
    ]
```

Run it:

```bash
python manage.py migrate
```

---

1. **Clean Up the Old Field**

- Remove the old `categories` field.
- Rename `categories_through` → categories.

Final model:

```python
class Post(models.Model):
    categories = models.ManyToManyField(to=Category, through="core.PostCategory")
```

Make and run the final migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

🎉 **Done!**

All your original M2M data has been safely migrated to a `through=` table, and your models are clean.
