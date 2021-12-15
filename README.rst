(Python OOP) ตัวอย่างการอัพโหลด package
=======================================

PyPi: https://pypi.org/project/oop_stpprofile/

วิธีติดตั้ง
~~~~~~~~~~~

เปิด CMD / Terminal

.. code:: python

   pip install oop_stpprofile

วิธีใช้งานแพ็คเพจนี้
~~~~~~~~~~~~~~~~~~~~

-  เปิด IDLE ขึ้นมาแล้วพิมพ์…

\```python from oop_stpprofile.Python_oop import Profile

my = Profile(“Suntipap”) my.company = “ublgroup” my.hobby =
[“Running”,“Python Programming”,“Game”] print(my.name) my.show_email()
my.show_hobby() print(“————”)

friend = Profile(“Sudchaya”) print(friend.name) friend.show_email()
my.show_myart()

#help(my)
