from django.contrib.auth.models import User
import threading
import time

# Define a signal

def user_saved_signal(sender, instance, created, **kwargs):
    print("Signal handler started in thread:", threading.get_ident())
    time.sleep(2)  # Delay to show the synchronous behavior
    print("Signal handler finished in thread:" , threading.get_ident())

# different caller
def simulate_different_caller():
    time.sleep(1)  # Delay to ensure the main thread has started
    print("Different caller started in thread:", threading.get_ident())
    user = User.objects.create(username='testuser')
    print("Different caller finished in thread:", threading.get_ident())

# Create a new thread
thread = threading.Thread(target=simulate_different_caller)
thread.start()

# Main thread continues 
print("Main thread started in thread:", threading.get_ident())
user = User.objects.create(username='testuser')
print("Main thread finished in thread:", threading.get_ident())

# Wait for thread to finish
thread.join()