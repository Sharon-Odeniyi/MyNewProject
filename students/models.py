from datetime import datetime
from django.db import models


class Department(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    matric_no = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT
    )

    class Meta:
        ordering = ["firstname", "lastname"]

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.matric_no}"

    @property
    def level(self):
        """
        Calculates the student's current academic level
        from the first two digits of the matric number.
        Example:
        20AH012234 -> Admission Year: 2020
        """

        try:
            current_year = datetime.now().year
            admission_year = 2000 + int(self.matric_no[:2])

            years = current_year - admission_year + 1

            # Limit level between 100 and 500
            if years <= 1:
                return "100 Level"
            elif years == 2:
                return "200 Level"
            elif years == 3:
                return "300 Level"
            elif years == 4:
                return "400 Level"
            else:
                return "500 Level"

        except (ValueError, IndexError):
            return "Unknown"