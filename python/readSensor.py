from os import curdir,sep,listdir
import os,sys
import cgi
import thread
import threading
import time
from time import sleep;
import smtplib;
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText;
from email.mime.multipart import MIMEMultipart;
from threading import Timer

#account setup
username = 'ev3devCEEO';
password = 'cee0prek!';
server = 'smtp.gmail.com:587';

# create msg - MIME* object
# takes addresses to, from cc and a subject
# returns the MIME* object
def create_msg(to_address,
               from_address='',
               cc_address='',
               bcc_address='',
               subject=''):
    
    msg = MIMEMultipart();
    msg['Subject'] = subject;
    msg['To'] = to_address;
    msg['Cc'] = cc_address;
    msg['From'] = from_address;
    return msg;

# send an email
# takes an smtp address, user name, password and MIME* object
# if mode = 0 sends to and cc
# if mode = 1 sends to bcc
def send_email(smtp_address, usr, password, msg, mode):
    server = smtplib.SMTP(smtp_address);
    server.ehlo();
    server.starttls();
    server.ehlo();
    server.login(username,password);
    if (mode == 0 and msg['To'] != ''):
        server.sendmail(msg['From'],(msg['To']+msg['Cc']).split(","), msg.as_string());
    elif (mode == 1 and msg['Bcc'] != ''):
        server.sendmail(msg['From'],msg['Bcc'].split(","),msg.as_string());
    elif (mode != 0 and mode != 1):
        print 'error in send mail bcc'; print 'email cancled'; exit();
    server.quit();

# compose email
# takes all the details for an email and sends it
# address format: list, [0] - to
#                       [1] - cc
#                       [2] - bcc
# subject format: string
# body format: list of pairs [0] - text
#                            [1] - type:
#                                        0 - plain
#                                        1 - html
# files is list of strings
def compose_email(addresses, subject, body, files):

    # addresses
    to_address = addresses[0];
    cc_address = addresses[1];
    bcc_address = addresses[2];

    # create a message
    msg = create_msg(to_address, cc_address=cc_address , subject=subject);

    # add text
    for text in body:
        attach_text(msg, text[0], text[1]);

    # add files
    if (files != ''):
        file_list = files.split(',');
        for afile in file_list:
            attach_file(msg, afile);

    # send message
    send_email(server, username, password, msg, 0);

    # check for bcc
    if (bcc_address != ''):
        msg['Bcc'] = bcc_address;
        send_email(server, username, password, msg, 1);
        
    print 'email sent'

# attach text
# attaches a plain text or html text to a message
def attach_text(msg, atext, mode):
    part = MIMEText(atext, get_mode(mode));
    msg.attach(part);

# util function to get mode type
def get_mode(mode):
    if (mode == 0):
        mode = 'plain';
    elif (mode == 1):
        mode = 'html';
    else:
        print 'error in text kind'; print 'email cancled'; exit();
    return mode;

# attach file
# takes the message and a file name and attaches the file to the message
def attach_file(msg, afile):
    part = MIMEApplication(open(afile, "rb").read());
    part.add_header('Content-Disposition', 'attachment', filename=afile);
    msg.attach(part);


 
#try to send an email every minute
def sendmail(string):
	compose_email(['jscolnic@gmail.com, jennethoma@gmail.com', '', '' ],
		'testing',
		[[string,0]],
		'');           

#sensor definitions

sensorpath = '/sys/class/lego-sensor/{}/'
sensorValue = sensorpath + 'value0'
sensorAttached = '/sys/class/lego-sensor/'
checkSensorPort = sensorpath + 'port_name'
drivername = sensorpath + 'driver_name'

def readSensors():
# sensor dictionary {'actual Ev3 port':'sensor0'}
	existingSensors = os.listdir(sensorAttached)
	SENSORS = {} # reset dictionary
	theValue = 0 
	for i in range(0,len(existingSensors)):
		try:
			senRead = open(checkSensorPort.format(existingSensors[i])) 
			mo = senRead.read()
			senRead.close
			SENSORS[mo[2]] = existingSensors[i] # add to dictionary
		except IOError:
			print "no sensor"

	for i in range(0,len(existingSensors)):
		# read sensor value
		n = str(i+1)
		Sens = open(sensorValue.format(SENSORS[n]))
		theValue = Sens.read()
		Sens.close
	return theValue

prevValue = 0
count = 0
while True:
	value = readSensors()
	if value > prevValue:
		count = count + 1
		if count == 1:
			string = "button pressed " + str(count) + " time."
			print "button pressed %d time." % count
		else:
			string = "button pressed " + str(count) + " times."
			print "button pressed %d times." % count
		# send email	
		sendmail(string);
	prevValue = value

