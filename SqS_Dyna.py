import tkinter
import boto3

from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("MIT-AOE Mess")
var = StringVar()
label = Label(root, textvariable=var, bg="pink", width=20, font=("bold", 10),bd=5, justify=RIGHT, padx=10, pady=10)
var.set("MIT-AOE Mess")
label.pack()
fields = ('Name', 'Contact', 'Address', 'Payment', 'Mess for','Joining_Date')


def monthly_payment(entries ):
    # variable
    global a, b, c, d, f ,k
    a = str(entries['Name'].get())
    b = str(entries['Contact'].get())
    c = str(entries['Address'].get())
    d = str(entries['Payment'].get())
    f = str(entries['Mess for'].get())
    k = str(entries['Joining_Date'].get())
    print(a)
    print(b)
    print(c)
    print(d)
    print(f)


def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=20, font=("bold", 10),text=field + ": ", anchor='w')
        ent = Entry(row)
        ent.insert(0, "0")
        row.pack(side=TOP, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES)
        entries[field] = ent
    return entries


if __name__ == '__main__':
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))

    b2 = Button(root, text='Submit', width=20, bg='green', fg='white',command=(lambda e=ents: monthly_payment(e)))
    b2.pack(side=LEFT, padx=5, pady=5)
    b3 = Button(root, text='Quit', width=20, bg='green', fg='white', command=root.quit)
    b3.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()
# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/278460603394/sqs-lambda-dynamodb-demo'

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'The Whistler'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'John Grisham'
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        }
    },
    MessageBody=(
            '{"user_id":"' + a + '","device":"' + b + '","location":"' + c + '","price":"' + d + '","time":"' + f + '" ,"join":"' + k + '"}'
    )
)

print(response['MessageId'])