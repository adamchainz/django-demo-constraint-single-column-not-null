django-demo-constraint-single-column-not-null
=============================================

Source code for my blog post `Using Django Check Constraints to Ensure Only One Field Is Set <https://adamj.eu/tech/2020/03/25/django-check-constraints-one-field-set/>`__.

Tested with Django 3.0 and Python 3.8.
Run these commands to try it out:

.. code-block:: console

    python -m venv venv
    source venv/bin/activate
    pip install django ipython
    python manage.py migrate
    python manage.py shell
