#Email simulator
import datetime
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False #by default, all the email are unread

    def mark_as_read(self): #method for change a email from unread to read
        self.read = True

    def display_full_email(self): #method that display the email
        self.mark_as_read() #call the method mark_as_read
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    def __str__(self): #return a string with the email status, sender name, subject and the timestamp
        status = 'Read' if self.read else 'Unread' #if statement for assign Read or Unread status in base to the self.read boolean value
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
    

class Inbox:
    def __init__(self):
        self.emails = [] #a list with email objects

    def receive_email(self, email): #method for receive an email and append to the emails list
        self.emails.append(email)

    def list_emails(self): #method for list all the emails
        if not self.emails: #check if the emails list is empty; self.emails is False if the list is empty
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1): #iterate in a tuple with listed emails objects
            print(f'{i}. {email}') #display the email obejct and his ordinal number

    def read_email(self, index): #method for select a email object from a list and display them
        if not self.emails: #check if the emails list is empty
            print('Inbox is empty.\n')
            return
        actual_index = index - 1 #substract 1 to the index parameter for be able to access the first object in the list
        if actual_index < 0 or actual_index >= len(self.emails): #check if the index value is out of range and print a message
            print('Invalid email number.\n')
            return
        #access to the email object in the emails list with the specified index and call the method display_full_email from Email class
        self.emails[actual_index].display_full_email() 

    def delete_email(self, index): #method for delete an email 
        if not self.emails: #check if the emails list is empty
            print('Inbox is empty.\n')
            return
        actual_index = index - 1 #substract 1 to the index parameter for be able to access the first object in the list
        if actual_index < 0 or actual_index >= len(self.emails): #check if the index value is out of range and print a message
            print('Invalid email number.\n')
            return
        del self.emails[actual_index] #delete an email object from emails list; access to the email object with the index value
        print('Email deleted.\n')
        

class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox() #each User has a Inbox where the emails are stored

    def send_email(self, receiver, subject, body): #method for send an email
        email = Email(sender=self, receiver=receiver, subject=subject, body=body) #create an email object with the atributes specified in the class

        #the email object is sent to a User object (receiver); the method receive_email from inbox class append the email object to emails list (User receiver object)
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    def check_inbox(self): #method for check the inbox
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails() #call the list_emails method from inbox class

    def read_email(self, index): #method for read a email
        self.inbox.read_email(index) #call the read_email object from inbox class

    def delete_email(self, index): #method for delete a email
        self.inbox.delete_email(index) #call the delete_email method from inbox class

jhon = User('Jhon')
steven = User('Steven')

#Jhon le envia a Steven tres emails
jhon.send_email(steven, 'Asunto importante', 'este es un asunto importante')
jhon.send_email(steven, 'Reunion laboral', 'tal dia tenemos una reunion laboral')
jhon.send_email(steven, 'Reunion familiar', 'la proxima semana tenemos una reunion familiar')

steven.check_inbox()
steven.read_email(4)
steven.read_email(3)
steven.check_inbox()
steven.delete_email(2)
steven.check_inbox()


#def main(): #standard Python idiom
#    tory = User('Tory')
#    ramy = User('Ramy')        
    
#    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
#    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    
#    ramy.check_inbox()
#    ramy.read_email(1)
#    ramy.delete_email(1)
#    ramy.check_inbox()
