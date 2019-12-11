import random
import string
from .models import Company


# generates a 15 digit invite code for a company
def generate_invite_code():
	invite_code = None

	while invite_code == None:
		# generates a random 15 digit string
		random_string = ''.join(
			[random.choice(string.ascii_letters + string.digits) for n in range(15)]
		)

		# if the random string does not already exists as an invite code
		if not Company.objects.filter(invite_code=random_string).exists():
			invite_code = random_string

	return invite_code



