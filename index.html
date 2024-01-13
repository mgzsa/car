import pywebio
import tabulate
from pywebio import start_server
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from datetime import date, timedelta, datetime
from tinydb import TinyDB, Query
from functools import partial
import time
import re
import argparse
import json

from  pywebio.pin import *
import pywebio.output as out

app = Flask(__name__)

# Initialize Flask object

# Initialize TinyDB




import urllib.request, json

#db = TinyDB('/Users/mac/Desktop/db.json')

import requests
import requests

import json



db = TinyDB('db.json')

User = Query()
users = db.table('USERS')
bookings = db.table('BOOKINGS')
def welcome():



    clear()

    img = open('car.png', 'rb').read()
    with use_scope('scope1', clear=True):
        put_image(img)
    put_text("")




    # Choose from either login or signup
    choose_onboarding = actions('', ['دخول', 'تسجيل'],
                                help_text='Choose one of the options to proceed.')

    if choose_onboarding == 'دخول':
        login()
    else:
        signup()


    """
    Car Booking Application

    Book a ride with our handsome drivers.
    Displays the welcome options for the car booking app. Would require users to either login or signup.

    Returns:
            None
    """


def login():

    '''
    Login options for existing users.

    Returns:
            None
    '''
    credentials = input_group("دخول المشتركين", [
        input('اسم المستخدم', name='username', type=TEXT,
              required=True, PlaceHolder="@username"),
        input('كلمة المرور', name='password', type=PASSWORD,
              required=True, PlaceHolder="Password"),
        actions('', [
            {'label': 'التالي', 'value': 'Save'},
            {'label': 'إلغاء', 'type': 'cancel', 'color': 'danger'},
        ], name='action', help_text=''),
    ])
    if credentials is not None:
        if credentials['action'] == 'Cancel':
            put_text('Cancel')

        else:

          # Checks for existing users that matches the username
          results = users.search(User.username == credentials['username'])
          print(results)

          # Checks the password and the user type
          if len(results) == 1 and results[0].get("password") == credentials['password']:
              if results[0].get("user_type") == 'admin':
                  admin_options(credentials['username'], results[0].get("name"))
              elif results[0].get("user_type") == 'driver':
                  driver_options(credentials['username'], results[0].get("name"))
              else:
                  user_options(credentials['username'], results[0].get("name"))
          else:
              popup("تنبيه", "تأكد من اسم المستخدم وكلمة المرور",
                    closable=True)
              welcome()


def signup():
    """
    Sign up page / option for new users.

    Returns:
            None
    """
    import json
    info = input_group('مستخدم جديد', [
        input('اسم المستخدم', name='username', type=TEXT,
              required=True, PlaceHolder="@username", validate=check_username),

        input('كلمة المرور', name='password', type=PASSWORD,
              required=True, PlaceHolder="Password"),

        input('تأكيد كلمة المرور', name='password_c', type=PASSWORD,
              required=True, PlaceHolder="Confirm Password"),

        input('الاسم الثلاثي', name='name', type=TEXT, required=True,
              PlaceHolder="name"),

        input('رقم الجوال', name='phone', type=NUMBER,
              required=True, PlaceHolder="05********"),

        input('البريد الإلكتروني', name='email', type=TEXT,
              required=True, PlaceHolder="user@gmail.com"),

        input('تاريخ المبلاد: ', name='birthdate', type=DATE,
              PlaceHolder="23/09/1993"),
        radio("نوع المشترك",name='User_Type', options=['Driver', 'Passenger'], required=True),
        checkbox("",name='agree', options=[
            'أوافق على الشروط'], required=True),

        actions('', [
            {'label': 'التالي', 'value': 'Save'},
            {'label': 'إلغاء', 'type': 'cancel', 'color': 'danger'},
        ], name='action', help_text=''),
    ])
    if info is not None:
        if info['action'] == 'Cancel':
            welcome()

        else:

             if info['agree'][0] == 'أوافق على الشروط':
                 last_row = users.get(doc_id=len(users))
                 #print(last_row["user_id"])





                 new_user_id = int(last_row["user_id"]) +1
                 users.insert({'user_id': new_user_id,
                               'username': info['username'],
                               'name': info['name'],
                               'password': info['password'],
                               'phone': info['phone'],
                               'email': info['email'],
                               'birthdate': info['birthdate'],
                               'user_type':info['User_Type'].lower()})

                 # Proceed to specific options per user but if the user is
                 # not a driver, then proceed to creating a ride.

             elif info['agree']!= 'أوافق على الشروط':
                 popup('تنبيه',['يجب الموافقة على الشروط'])
             if info['User_Type'].lower() == 'driver':
                     driver_options(info['username'], info['name'])
             else:
                     create_ride(info['username'], info['name'])
                     user_options(info['username'], info['name'])

    welcome()

def driver_options(name,username):


    #put_html('<marquee>\n</marquee>')

    admin_task = actions(f"{'السائق'}\n{name}",['خروج','الطلبات المكتملة','الطلبات الحالية','الطلبات الجديدة','حجز جديد'])
#                         help_text='Choose one of the options to proceed.')
    # put_buttons([dict(label='Home', value='s', color='success')], onclick=admin_options(username, name))
    if admin_task == 'حجز جديد':
        clear()
        create_ride(username,name)
        driver_options(username,name)
    elif admin_task == 'خروج':
        clear()
        welcome()
    elif admin_task == 'الطلبات الجديدة':
        clear()


        for row in bookings:
            if row['assigned_driver'] == username and row['status'] =='مقبول'or row['status'] == 'معاد من الإدارة':
            #    popup("يوجد لديك طلب غير مكتمل",f"\n{put_table([[row['name'],'name']],)}")

                popup("يوجد لديك طلبات غير مكتمل ",'')
                break
        display_table = [
                ['خيارات','وقت القبول', 'تاريخ القبول', 'السائق', 'حالة الحجز', 'الملاحظة', 'الوجهة', 'الوقت', 'بداية الحجز','المشترك']]
        for row in bookings:
            if row['status'] =='جديد':
                    display_table.append([
                        put_buttons(['اقبل'], onclick=partial(update_driver, row=row, username=username, name=name)),

                        row['end_time'],
                        row['end_date'],

                        row['assigned_driver'],
                        row['status'],

                        row['destination'],

                        row['remarks'],

                        row['time'],

                        row['date'],

                        row['name'], ])
                    print(row)
        put_table([[len(display_table) - 1, ":عدد الطلبات "]])

        put_table(display_table)
        driver_options(username,name)



    elif admin_task == 'الطلبات الحالية':
        clear()

        display_table = [
            ['خيارات', 'وقت القبول', 'تاريخ القبول', 'السائق', 'حالة الحجز', 'الملاحظة', 'الوجهة', 'الوقت',
             'بداية الحجز','المشترك' ]]
        for row in bookings:
            if row['assigned_driver'] == username:
                 if row['assigned_driver'] == username and row['status'] == 'مقبول' or row['status'] == 'معاد إلى السائق'or  row['status'] == 'الراكب معترض':

                     display_table.append([
                         put_buttons(['إنهاء'], onclick=partial(update_status, row=row, username=username, name=name)),

                         row['end_time'],
                         row['end_date'],

                         row['assigned_driver'],
                         row['status'],

                         row['destination'],

                         row['remarks'],

                         row['time'],

                         row['date'],

                         row['name'], ])
        put_table([[len(display_table)-1,":عدد الطلبات "]])
        put_table(display_table)
        driver_options(username, name)
    elif admin_task == 'الطلبات المكتملة':
        clear()

        display_table = [
            [ 'وقت الانهاء', 'تاريخ الإنهاء', 'السائق', 'حالة الحجز', 'الملاحظة', 'الوجهة', 'الوقت',
             'بداية الحجز','المشترك' ]]
        for row in bookings:
            if row['assigned_driver'] == username and row['status'] == 'مكتمل'or  row['status'] == 'ملغي من قبل الراكب''مكتمل'or  row['status'] == 'ملغي من قبل الإدارة':
                display_table.append([
                    row['end_time'],
                    row['end_date'],

                    row['assigned_driver'],
                    row['status'],

                    row['destination'],

                    row['remarks'],

                    row['time'],

                    row['date'],

                    row['name'], ])



                print(row)
        # put_buttons([dict(label='Home', value='s', color='success')], onclick=admin_options(username, name))
        put_table([[len(display_table)-1,":عدد الطلبات "]])
        put_table(display_table)
        driver_options(username,name)


def edt_users(choice,name, row, username):
      # تعديل المشترك

    info = input_group('تعديل بيانات المستخدم', [
        #input('رقم المستخدم', name='user_id', type=TEXT, required=False, value=row['user_id']),

        #input('اسم المستخدم', name='username', type=TEXT,required=True, value=row['username'], validate=check_username_for_edt),

        input('كلم المرور', name='password', type=PASSWORD,
              required=True, value=row['password']),

        input('تأكيد كلمة المرور', name='password_c', type=PASSWORD,
              required=True, value=row['password']),

        input('الاسم الثلاثي', name='name', type=TEXT, required=True,
              value=row['name']),

        input('رقم الجوال', name='phone', type=NUMBER,
              required=True, value=row['phone']),

        input('البريد الإلكتروني', name='email', type=TEXT,
              required=True, value=row['email']),

        input('تاريخ المبلاد: ', name='birthdate', type=DATE,
              value=row['birthdate']),
        radio("نوع المشترك", name='User_Type', options=['admin','Driver', 'Passenger'], required=True),

        actions('', [
            {'label': 'التالي', 'value': 'Save'},
            {'label': 'إلغاء', 'type': 'cancel', 'color': 'danger'},
        ], name='action', help_text=''),])




    if info is not None:
        if info['action'] == 'Cancel':
           admin_options(username,name)

        else:

                    users.update({
                                  #'username': info['username'],
                                  'name': info['name'],
                                  'password': info['password'],
                                  'phone': info['phone'],
                                  'email': info['email'],
                                  'birthdate': info['birthdate'],
                                  'user_type': info['User_Type'].lower()}, User.user_id == row['user_id'])
                    results = bookings.search(User.username == row['username'])
                    popup('',['تم تحديث البيانات بنجاحll'])

                    if len(results) > 0:
                        username_bookings = results[0].get("username")

                        #print(username_bookings)

                        bookings.update({'name': info['name']}, User.username == username_bookings)

                    else:
                        popup('',['هذا المستخدم ليس لديه أي تفاعل في الموقع '])

                    display_table = [['حذف', 'تعديل', 'حجز', 'نوع المشترك', 'تاريخ الميلاد', 'البريد الإلكتروني', 'رقم الجوال',
                                  ' الرقم السري', 'اسم المستخدم', 'المشترك', 'رقم الاشتراك']]

                    for row in users:
                        clear()
                        display_table.append([
                            put_buttons(['احذف'],
                                        onclick=partial(delete_users, row=row, username=username, name=name)),
                            put_buttons(['عدل'],
                                        onclick=partial(edt_users, row=row, username=username, name=name)),

                            put_buttons(['احجز'],
                                        onclick=partial(create_ride_py_admin, row=row, username=username, name=name)),

                            row['user_type'],
                            row['birthdate'],
                            row['email'],
                            row['phone'],

                            row['password'],

                            row['username'],
                            row['name'],

                            row['user_id'],

                        ])

                    # put_buttons([dict(label='Home', value='s', color='success')], onclick=admin_options(username, name))
                    put_table(display_table)
                    put_table([[len(display_table) - 1, ":عدد المشتركين "]])


                    admin_options(username, name)






def check_username_for_edt(username):

    """
    Checks if there is already an existing username.

    Parameters:
        username (string): The username that was entered in the form and to be rechecked
            against existing usernames

    Returns:
        value (str): The error
'
    """


    results = users.search(User.username == username )
    if len(results) > 0:
        return 'اسم المستخدم موجد.'


def delete_booking(choice,name, row, username):
    results = bookings.search(User.username == row['username'])
    if len(results) > 0:
        username_bookings = results[0].get("username")
        bookings.remove(User.username == username_bookings)
    clear()
    display_table = [
        ['إلغاء', 'تغيير الوجهة', 'وقت الإجراء', 'تاريخ ', 'السائق', 'حالة الحجز', 'الملاحظة', 'الوجهة', 'الوقت',
         'بداية الحجز', 'المستخدم', 'المشترك']]
    for row in bookings:
        if row['status'] == "مكتمل":
            display_table.append([
                put_buttons(['حذف نهائي'], onclick=partial(delete_booking, row=row, username=username, name=name)),

                put_buttons(['اعده إلى السائق'],
                            onclick=partial(cancel_request, row=row, username=username, name=name)),

                row['end_time'],
                row['end_date'],

                row['assigned_driver'],
                row['status'],

                row['destination'],

                row['remarks'],

                row['time'],

                row['date'],
                row['username'],
                row['name'],

            ])
    put_table([[len(display_table) - 1, ":عدد الطلبات "]])
    # put_buttons([dict(label='Home', value='s', color='success')], onclick=admin_options(username, name))
    put_table(display_table)
    admin_options(username, name)



def delete_users(choice,name, row, username):
      # تعديل المشترك

    info = input_group('تعديل بيانات المستخدم',[
        actions('', [
            {'label': 'حذف', 'value': 'Save'},
            {'label': 'إلغاء', 'type': 'cancel', 'color': 'danger'},
        ], name='action', help_text=''),
                       ])
    if info is not None:
        if info['action'] == 'Cancel':
            admin_options(username, name)

        else:

            results = users.search(User.username == row['username'])
            user_type = ''
            if len(results) > 0:
                user_type = results[0].get("user_type")
            print("User " + user_type)
            if user_type == 'admin':
                popup('تنبيه',['!! لايمكن حذف المدير'])
            else:
                popup('نجاح الحذف',['تم الحذف بنجاح'])




                results = bookings.search(User.username == row['username'])
                if len(results) > 0:


                    username_bookings = results[0].get("username")
                    bookings.remove(User.username == username_bookings)
                users.remove(User.user_id == row['user_id'])
                display_table = [['حذف', 'تعديل', 'حجز', 'نوع المشترك', 'تاريخ الميلاد', 'البريد الإلكتروني', 'رقم الجوال',
                                  ' الرقم السري', 'اسم المستخدم', 'المشترك', 'رقم الاشتراك']]

                for row in users:
                    clear()
                    display_table.append([

                        put_buttons(['احذف'],
                                    onclick=partial(delete_users, row=row, username=username, name=name)),
                        put_buttons(['عدل'],
                                    onclick=partial(edt_users, row=row, username=username, name=name)),

                        put_buttons(['احجز'],
                                    onclick=partial(create_ride_py_admin, row=row, username=username, name=name)),

                        row['user_type'],
                        row['birthdate'],
                        row['email'],
                        row['phone'],

                        row['password'],

                        row['username'],
                        row['name'],

                        row['user_id'],

                    ])

                # put_buttons([dict(label='Home', value='s', color='success')], onclick=admin_options(username, name))
                put_table(display_table)
                put_table([[len(display_table) - 1, ":عدد المشتركين "]])

                admin_options(username, name)


def edt_remarks(choice, row, username, name):
    #تعديل الوجهة
    credentials = input_group("تغيير الوجهة", [
        input('الجهة الجديدة', name='note', type=TEXT,
              required=True),],cancelable=True)
    bookings.update({'remarks':credentials['note']},User.booking_id == row['booking_id'])

    print(credentials['note'])

    clear()
    display_table = [
        ['إلغاء', 'تغيير الوجهة', 'وقت الإجراء', 'تاريخ ', 'السائق', 'حالة الحجز', 'الملاحظة', 'الوجهة', 'الوقت',
         'بداية الحجز', 'المستخدم', 'المشترك']]
    for row in bookings:
        if row['status'] == "جديد":
            display_table.append([
                put_buttons(['إلغاء الطلب'],
                            onclick=partial(cancel_request, row=row, username=username, name=name)),
                put_buttons(['تغيير الوجه'], onclick=partial(edt_remarks, row=row, username=username, name=name)),

                row['end_time'],
                row['end_date'],

                row['assigned_driver'],
                row['status'],

                row['destination'],

                row['remarks'],

                row['time'],

                row['date'],
                row['username'],
                row['name'],

            ])

    # put_buttons([dict(label='Home', value='s', color='success')], onclick=admin_options(username, name))
    put_table([[len(display_table) - 1, ":عدد الطلبات "]])

    put_table(display_table)
    admin_options(username, name)

def update_driver(choice, row, username, name):
    """
    Update the driver of a particular booking.
    When the driver clicks on the Accept Booking button, this function would
    update the assigned driver.

    Parameters:
        choice (string): the choice or name of the button that was clicked
        row (dictionary): the whole row of the booking that needs updating
        username (string): username of the user in session
        name (string): their full name in the form

    Returns:
        None
    """

    put_text("You click %s button ar row %s" % (choice, row))
    bookings.update({'status': 'مقبول','assigned_driver':username,'end_date':datetime.now().strftime("%Y-%m-%d"),'end_time':datetime.now().strftime("%H:%M")}, User.booking_id == row['booking_id'])
    toast("تم القبول.")
    # username = row['username']
    # name = row['name']
    print(username, name)
    clear()
    display_table = [
        ['خيارات', 'وقت القبول', 'تاريخ القبول', 'السائق', 'حالة الحجز', 'الملاحظة', 'الوجهة', 'الوقت',
         'بداية الحجز','المشترك' ]]
    for row in bookings:
        if row['assigned_driver'] == username and  row['status'] == 'مقبول'or row['status'] == 'معاد إلى السائق':
            display_table.append([
                put_buttons(['إنهاء'], onclick=partial(update_status, row=row, username=username, name=name)),

                row['end_time'],
                row['end_date'],

                row['assigned_driver'],
                row['status'],

                row['destination'],

                row['remarks'],

                row['time'],

                row['date'],

                row['name'], ])
            print(row)
    # put_buttons([dict(label='Home', value='s', color='success')], onclick=admin_options(username, name))
    put_table([[len(display_table) - 1, ":عدد الطلبات "]])

    put_table(display_table)
    driver_options(username, name)


def update_status(choice, row, username, name):
    """
    Updates the status of a booking
    When the driver clicks on the Mark as Done button, this function will update
    the booking status as done.

    Parameters:
        choice (string): the choice or name of the button that was clicked
        row (dictionary): the whole row of the booking that needs updating
        username (string): username of the user in session
        name (string): their full name in the form

    Returns:
        None
    """

    put_text("You click %s button ar row %s" % (choice, row))
    bookings.update({'status': 'مكتمل','end_date':datetime.now().strftime("%Y-%m-%d"),'end_time':datetime.now().strftime("%H:%M")}, User.booking_id == row['booking_id'])
    toast("تم الانتهاء.")
    # username = row['username']
    # name = row['name']
    print(username, name)
    clear()
    display_table = [
        ['خيارات', 'وقت الإنهاء', 'تاريخ الإنهاء', 'السائق', 'حالة الحجز', 'الملاحظة', 'الوجهة', 'الوقت',
         'بداية الحجز','المشترك' ]]
    for row in bookings:
        if row['assigned_driver'] == username and  row['status'] == 'مقبول'or   row['status'] == 'معاد إلى السائق':
            display_table.append([
                put_buttons(['إنهاء'], onclick=partial(update_status, row=row, username=username, name=name)),

                row['end_time'],
                row['end_date'],

                row['assigned_driver'],
                row['status'],

                row['destination'],

                row['remarks'],

                row['time'],

                row['date'],

                row['name'], ])
            print(row)
    # put_buttons([dict(label='Home', value='s', color='success')], onclick=admin_options(username, name))
    put_table([[len(display_table) - 1, ":عدد الطلبات "]])

    put_table(display_table)
    driver_options(username, name)


def user_options(username, name):
    """
    Options for user type: passenger
    The passengers are allowed to
        (1) View all bookings (booking where username = passenger)
        (2) Book a ride for themselves

    Parameters:
        username (string): username of the user in session
        name (string): Their full name in the form

    Returns:
        None
    """
    admin_task = actions(f'الراكب:{name}',
                         [ 'خروج', 'الطلبات الملغية', 'الطلبات المكتملة','الطلبات الجديدة', 'حجز جديد'],
                         help_text='Choose one of the options to proceed.')
    # put_buttons([dict(label='Home', value='s', color='success')], onclick=admin_options(username, name))

    if admin_task == 'حجز جديد':
        clear()
        create_ride(username, name)
        user_options(username, name)
    elif admin_task == 'خروج':
        clear()
        welcome()
    elif admin_task == 'الطلبات الجديدة':
        clear()
        display_table = [['إلغاء الطلب','حالة الحجز', 'الملاحظة',  'الوجهة', 'الوقت', 'بداية الحجز', 'المشترك' ]]

        for row in bookings:
            if row['username'] == username:
                if row['username'] == username and row['status'] == 'جديد' or row['status'] == 'مقبول':
                    display_table.append([
                        put_buttons(['إلغاء الطلب'], onclick=partial(cancel_request, row=row, username=username, name=name)),

                        row['status'],

                        row['destination'],

                        row['remarks'],

                        row['time'],

                        row['date'],

                        row['name'],

                    ])

        put_table([[len(display_table)-1,":عدد الطلبات "]])
        put_table(display_table)

        user_options(username, name)
    elif admin_task == 'الطلبات المكتملة':
        clear()
        display_table = [['خيارات', 'وقت الاكتمال','تاريخ الاكتمال','السائق','حالة الحجز', 'الملاحظة',  'الوجهة', 'الوقت', 'بداية الحجز', 'المشترك']]
        for row in bookings:
            if row['username'] == username:

                if row['username'] == username and row['status'] == 'مكتمل'or row['status'] == 'الراكب معترض':
                    display_table.append([
                        put_buttons(['تقديم اعتراض'],
                                    onclick=partial(cancel_request, row=row, username=username, name=name)),
                        row['end_time'],
                        row['end_date'],

                        row['assigned_driver'],
                        row['status'],

                        row['destination'],

                        row['remarks'],

                        row['time'],

                        row['date'],

                        row['name'],

                    ])

        put_table([[len(display_table)-1,":عدد الطلبات "]])
        put_table(display_table)

        user_options(username, name)
    elif admin_task == 'الطلبات الملغية':
        clear()
        display_table = [['وقت الإلغاء','تاريخ الإلغاء','السائق','حالة الحجز', 'الملاحظة',  'الوجهة', 'الوقت', 'بداية الحجز', 'المشترك']]
        for row in bookings:
            if row['username'] == username:
                if row['username'] == username and row['status'] == 'ملغي من قبل الراكب' or row[
                    'status'] == 'ملغي من قبل الإدارة' or row['status'] == 'معاد إلى السائق' :
                    display_table.append([
                        row['end_time'],
                        row['end_date'],

                        row['assigned_driver'],
                        row['status'],

                        row['destination'],

                        row['remarks'],

                        row['time'],

                        row['date'],

                        row['name'],

                    ])

        put_table([[len(display_table)-1,":عدد الطلبات "]])
        put_table(display_table)

        user_options(username, name)


def cancel_request(choice, row, username, name):
    """
    Update the status of a booking to cancelled

    Parameters:
        choice (string): the choice or name of the button that was clicked
        row (dictionary): the whole row of the booking that needs updating
        username (string): username of the user in session
        name (string): their full name in the form

    Returns:
        None
    """
    # put_text("You click %s button ar row %s" % (choice, row))
    results = users.search(User.username == username)
    user_type = ''
    if len(results) > 0:
        user_type = results[0].get("user_type")
    print("User " + user_type)
    if user_type == 'passenger':
        if row['status'] == "جديد" or row['status'] == "مقبول":
            bookings.update({'status': 'ملغي من قبل الراكب','end_date':datetime.now().strftime("%Y-%m-%d"),'end_time':datetime.now().strftime("%h:%m")}, User.booking_id == row['booking_id'])
            toast("تم إلغاء الطلب")

        else:

            bookings.update({'status': 'الراكب معترض','end_date':datetime.now().strftime("%Y-%m-%d"),'end_time':datetime.now().strftime("%h:%m")}, User.booking_id == row['booking_id'])
            toast("تم الاعتراض على الطلب ")

    elif user_type == 'admin':
        if row['status'] == "الراكب معترض":
            bookings.update({'status': 'معاد إلى السائق','end_date':datetime.now().strftime("%Y-%m-%d"),'end_time':datetime.now().strftime("%h:%m")}, User.booking_id == row['booking_id'])
            toast("تم إعادة الطلب إلى السائق")
        elif row['status'] == "مكتمل":
            bookings.update({'status': 'معاد إلى السائق','end_date':datetime.now().strftime("%Y-%m-%d"),'end_time':datetime.now().strftime("%h:%m")}, User.booking_id == row['booking_id'])
            toast("تم إعادة الطلب إلى السائق")


        else:
            bookings.update({'status': 'ملغي من قبل الإدارة','end_date':datetime.now().strftime("%Y-%m-%d"),'end_time':datetime.now().strftime("%H:%H")}, User.booking_id == row['booking_id'])
            toast("تم إلغاء الطلب")
    # username = row['username']
    # name = row['name']
    print(username, name)
    clear()

    if user_type == 'passenger':
        user_options(username, name)
    elif user_type == 'admin':

        admin_options(username, name)


def admin_options(username,name):
    """
    Options for user type: admin
    The drivers are allowed to
        (1) View all bookings
        (2) View all users
        (3) Book a ride for themselves

    Parameters:
        username (string): username of the user in session
        name (string): Their full name in the form

    Returns:
        None
    """
    admin_task = actions(f'{name}',['خروج','المشتركين','جميع الطلبات','الاعتراضات','الطلبات المكتملة', 'الطلبات المقبولة', 'الطلبات الجديدة'])



# put_buttons([dict(label='Home', value='s', color='success')], onclick=admin_options(username, name))

    if admin_task == 'المشتركين':
        credentials = input_group("ابحث عن مشترك", [

            input('الاسم', name='name', type=TEXT,
                  required=False), actions('', [
                {'label': 'بحث', 'value': 'Save', 'color': '#43766C'}, ], name='action', help_text=''), ])
        if credentials['action'] == 'Save':
            display_table = [['حذف','تعديل', 'حجز', 'نوع المشترك', 'تاريخ الميلاد', 'البريد الإلكتروني', 'رقم الجوال', ' الرقم السري', 'اسم المستخدم', 'المشترك', 'رقم الاشتراك']]

            for row in users:
                clear()

                if credentials['name']in(row['name']):

                    display_table.append([
                        put_buttons(['احذف'],
                                    onclick=partial(delete_users, row=row, username=username, name=name)),
                        put_buttons(['عدل'],
                                    onclick=partial(edt_users, row=row, username=username, name=name)),

                        put_buttons(['احجز'],
                                    onclick=partial(create_ride_py_admin, row=row, username=username, name=name)),

                        row['user_type'],
                        row['birthdate'],
                        row['email'],
                        row['phone'],

                        row['password'],

                        row['username'],
                        row['name'],

                        row['user_id'],

                    ])


            put_table(display_table)
            put_table([[len(display_table) - 1, ":عدد المشتركين "]])
            admin_options(username, name)








    elif admin_task == "جميع الطلبات":
        clear()
        display_table = [['حذف نهائي','وقت الإجراء','تاريخ الإجراء','السائق','حالة الحجز', 'الملاحظة',  'الوجهة', 'الوقت', 'بداية الحجز','المستخدم', 'المشترك']]
        for row in bookings:

            display_table.append([
                put_buttons(['حذف نهائي'], onclick=partial(delete_booking, row=row, username=username, name=name)),

                row['end_time'],
                row['end_date'],

                row['assigned_driver'],
                row['status'],

                row['destination'],

                row['remarks'],

                row['time'],

                row['date'],
                row['username'],
                row['name'],

            ])

        # put_buttons([dict(label='Home', value='s', color='success')], onclick=admin_options(username, name))
        put_table([[len(display_table)-1,":عدد الطلبات "]])
        put_table(display_table)



        admin_options(username, name)
    elif admin_task == "الطلبات الجديدة":
        clear()
        display_table = [['إلغاء','تغيير الوجهة','وقت الإجراء','تاريخ ','السائق','حالة الحجز', 'الملاحظة',  'الوجهة', 'الوقت', 'بداية الحجز', 'المستخدم','المشترك']]
        for row in bookings:
            if row['status']=="جديد":
                display_table.append([

                    put_buttons(['إلغاء الطلب'],
                                onclick=partial(cancel_request, row=row, username=username, name=name)),
                    put_buttons(['تغيير الوجه'], onclick=partial(edt_remarks, row=row, username=username, name=name)),


                    row['end_time'],
                    row['end_date'],

                    row['assigned_driver'],
                    row['status'],

                    row['destination'],

                    row['remarks'],

                    row['time'],

                    row['date'],
                    row['username'],
                    row['name'],



                        ])


        put_table([[len(display_table)-1,":عدد الطلبات "]])
        put_table(display_table)
        admin_options(username, name)
        #put_buttons([dict(label='Home', value='s', color='success')], onclick=admin_options(username, name))

    elif admin_task == "الطلبات المقبولة":
        clear()
        display_table = [['إلغاء','تغيير الوجهة','وقت الإجراء','تاريخ ','السائق','حالة الحجز', 'الملاحظة',  'الوجهة', 'الوقت', 'بداية الحجز', 'المستخدم','المشترك']]
        for row in bookings:
            if row['status'] == "مقبول"or row['status']=='معاد إلى السائق':

                display_table.append([
                    put_buttons(['إلغاء الطلب'],
                                onclick=partial(cancel_request, row=row, username=username, name=name)),
                    put_buttons(['تغيير الوجه'], onclick=partial(edt_remarks, row=row, username=username, name=name)),

                    row['end_time'],
                    row['end_date'],

                    row['assigned_driver'],
                    row['status'],

                    row['destination'],

                    row['remarks'],

                    row['time'],

                    row['date'],

                    row['username'],
                row['name'],


                ])


        #put_buttons([dict(label='Home', value='s', color='success')], onclick=admin_options(username, name))

        put_table([[len(display_table)-1,":عدد الطلبات "]])
        put_table(display_table)
        #put_buttons([dict(label='Home', value='s', color='success')], onclick=admin_options(username, name))

        admin_options(username, name)
    elif admin_task == "الطلبات المكتملة":
        clear()
        display_table = [['إلغاء','تغيير الوجهة','وقت الإجراء','تاريخ ','السائق','حالة الحجز', 'الملاحظة',  'الوجهة', 'الوقت', 'بداية الحجز', 'المستخدم','المشترك']]
        for row in bookings:
            if row['status'] == "مكتمل":
                display_table.append([
                    put_buttons(['حذف نهائي'], onclick=partial(delete_booking, row=row, username=username, name=name)),

                    put_buttons(['اعده إلى السائق'],
                                onclick=partial(cancel_request, row=row, username=username, name=name)),

                    row['end_time'],
                    row['end_date'],

                    row['assigned_driver'],
                    row['status'],

                    row['destination'],

                    row['remarks'],

                    row['time'],

                    row['date'],
                    row['username'],
                row['name'],


                ])
        put_table([[len(display_table)-1,":عدد الطلبات "]])
        # put_buttons([dict(label='Home', value='s', color='success')], onclick=admin_options(username, name))
        put_table(display_table)
        admin_options(username, name)
    elif admin_task == "الاعتراضات":
        clear()
        display_table = [['إلغاء','تغيير الوجهة','وقت الإجراء','تاريخ ','السائق','حالة الحجز', 'الملاحظة',  'الوجهة', 'الوقت', 'بداية الحجز','المستخدم', 'المشترك']]
        for row in bookings:
            if row['status'] == "الراكب معترض":
                display_table.append([
                    put_buttons(['اعده إلى السائق'],
                                onclick=partial(cancel_request, row=row, username=username, name=name)),
                    put_buttons(['تغيير الوجه'], onclick=partial(edt_remarks, row=row, username=username, name=name)),

                    row['end_time'],
                    row['end_date'],

                    row['assigned_driver'],
                    row['status'],

                    row['destination'],

                    row['remarks'],

                    row['time'],

                    row['date'],
                    row['username'],
                row['name'],


                ])
                print(row)
        put_table([[len(display_table)-1,":عدد الطلبات "]])
        # put_buttons([dict(label='Home', value='s', color='success')], onclick=admin_options(username, name))
        put_table(display_table)
        admin_options(username, name)
    elif admin_task == "خروج":
        clear()
        welcome()


def check_form(user_data):
    """
    This function is used for validating the data being entered in the user
    signup form.

    Parameters:
        user_data (dictionary): the data being typed in the form

    Returns:
        value (str): The error message to be sent
    """
    # For checking Email, whether Valid or not.
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    # For checking Names
    if user_data['name'].isdigit():
        return ('name', 'Invalid name! Name should not be numeric.')

    # For checking Email
    if not (re.search(regex, user_data['email'])):
        return ('email', 'Invalid email!')

    # For matching Passwords
    if user_data['password'] != user_data['password_c']:
        return ('password_c', "Please make sure your passwords match.")


def create_ride(username,name):
    """
    Form for creating a ride / booking request

    Parameters:
        username (string): username of the user in session
        name (string): Their full name in the form

    Returns:
        None
    """

    # print(bookings[len(bookings)]["booking_id"])

    last_row = bookings.get(doc_id=len(bookings))
    contbok = len(bookings)
    print(contbok)
    if contbok == 0:
        new_booking_id = 1
    else:

    #print(last_row["booking_id"])
    # Creates a form in pywebio that allows users to enter booking details
        new_booking_id = int(last_row["booking_id"]) + 1
    ride_details = input_group("قم بتعبئية البيانات لإكمال الحجز", [
        input('الاسم: ', name='name', placeholder='First, Last', value=name),

        input('اسم المستخدم: ', name='username', readonly=False, placeholder=username, value=username),
        input('تاريخ الحجز: ', name='booking_date', type=DATE, validate=check_booking_date,value=datetime.now().strftime("%Y-%m-%d")),
        input('الوقت: ', name='booking_time', type=TIME,validate=check_booking_time, value=datetime.now().strftime("%H:%M")),
        input('الملاحظة:', name='booking_destination'),
        input('الوجهة:', name='booking_remarks'),
       actions('', [
            {'label': 'التالي', 'value': 'Save'},
            {'label': 'إلغاء', 'type': 'cancel', 'color': 'danger'},
        ], name='action', help_text=''),
    ])
    if ride_details is not None:
        if ride_details['action'] == 'Cancel':
            put_text('Cancel')
            welcome()
        else:





            print(ride_details['booking_date'], ride_details['booking_time'])

            # Inserts what was entered into the TinyDB db.json
            bookings.insert({'booking_id': new_booking_id,
                             'username': ride_details['username'],
                             'name': ride_details['name'],
                             'date': ride_details['booking_date'],  # string(datetime.date(datetime.now())),
                             'time': ride_details['booking_time'],  # string(datetime.time(datetime.now())),
                             'destination': ride_details['booking_destination'],
                             'remarks': ride_details['booking_remarks'],
                             'status': 'جديد',
                             'assigned_driver':'',
                             'end_date': '0',
                             'end_time': '0',


                             })


            popup("طلبك مؤكد",
                  f"\nتفاصيل الطلب  "
                  f"\n الوجهة: {ride_details['booking_remarks']}\n"
                  f"التاريخ:{str(ride_details['booking_date'])}"
                  f"\nالوقت : {ride_details['booking_time']}"
                  f"\nالملاحظة: {ride_details['booking_destination']}",
                  closable=True)


            # Checks for existing users that matches the username

            # Checks the password and the user type




def create_ride_py_admin(choice, row, username, name):
    """
    Form for creating a ride / booking request

    Parameters:
        username (string): username of the user in session
        name (string): Their full name in the form

    Returns:
        None
    """

    # print(bookings[len(bookings)]["booking_id"])
    last_row = bookings.get(doc_id=len(bookings))

    if last_row == None:
        popup('مرحبا',['سيكون هذا الحجز هو الحجز الأول '])
        new_booking_id = 1
    else:
        new_booking_id = int(last_row["booking_id"]) + 1

    #print(last_row["booking_id"])
    # Creates a form in pywebio that allows users to enter booking details
    #new_booking_id = int(last_row["booking_id"]) + 1
    ride_details = input_group("قم بتعبئية البيانات لإكمال الحجز", [
        input('الاسم: ', name='name', placeholder='First, Last', value=row['name']),
        input('اسم المستخدم: ', name='username', readonly=False, placeholder=username, value=row['username']),
        input('تاريخ الحجز: ', name='booking_date', type=DATE, validate=check_booking_date,value=datetime.now().strftime("%Y-%m-%d")),
        input('الوقت: ', name='booking_time', type=TIME,validate=check_booking_time, value=datetime.now().strftime("%H:%M")),
        input('الملاحظة:', name='booking_destination'),
        input('الوجهة:', name='booking_remarks'),
       actions('', [
            {'label': 'التالي', 'value': 'Save'},
            {'label': 'إلغاء', 'type': 'cancel', 'color': 'danger'},
        ], name='action', help_text=''),
    ])
    if ride_details is not None:
        if ride_details['action'] == 'Cancel':
           welcome()



        else:





            print(ride_details['booking_date'], ride_details['booking_time'])

            # Inserts what was entered into the TinyDB db.json
            bookings.insert({'booking_id': new_booking_id,
                             'username': ride_details['username'],
                             'name': ride_details['name'],
                             'date': ride_details['booking_date'],  # string(datetime.date(datetime.now())),
                             'time': ride_details['booking_time'],  # string(datetime.time(datetime.now())),
                             'destination': ride_details['booking_destination'],
                             'remarks': ride_details['booking_remarks'],
                             'status': 'جديد',
                             'assigned_driver':'',
                             'end_date': '0',
                             'end_time': '0',


                             })


            popup("طلبك مؤكد",
                  f"\nتفاصيل الطلب  "
                  f"\n الوجهة: {ride_details['booking_remarks']}\n"
                  f"التاريخ:{str(ride_details['booking_date'])}"
                  f"\nالوقت : {ride_details['booking_time']}"
                  f"\nالملاحظة: {ride_details['booking_destination']}",
                  closable=True)
    admin_options(username,name)


def show_ride_request(ride_details):
    """
    Places the ride details in a table format

    Parameters:
        ride_details (dictionary): The ride details in dictionary format

    Returns:
        None
    """
    put_table([['Name', 'User ID', 'Date', 'Time'], [
        ride_details['name'], ride_details['username'],
        ride_details['booking_date'], ride_details['booking_time']]])

def check_username(username):
    """
    Checks if there is already an existing username.

    Parameters:
        username (string): The username that was entered in the form and to be rechecked
            against existing usernames

    Returns:
        value (str): The error message
    """

    results = users.search(User.username == username)
    if len(results) > 0:
        return 'اسم المستخدم موجد.'

def check_booking_date(booking_date):
    """
    Checks the value of the booking_date entered.

    Parameters:
        booking_date (string): The booking date that was entered in the form

    Returns:
        value (str): The error message
    """

    entered_day = datetime.strptime(booking_date, "%Y-%m-%d")
    present_day = datetime.now()
    if entered_day.date() < present_day.date():
        return 'Choose a better date'
def check_booking_time(booking_time):
    """
    Checks the value of the booking_date entered.

    Parameters:
        booking_date (string): The booking date that was entered in the form

    Returns:
        value (str): The error message
    """

    entered_time = datetime.strptime(booking_time, "%H:%M")
    present_time =datetime.now()


    if entered_time.time() < present_time.time():
        return 'لا يمكن الحجز في وقت منتهي'


def set_now_ts(set_value):
    set_value(int(time.time()))


def select_date(set_value):
    with popup('Select Date'):
        put_buttons(['Today'], onclick=[lambda: set_value(date.today(), 'Today')])
        put_buttons(['Yesterday'], onclick=[lambda: set_value(date.today() - timedelta(days=1), 'Yesterday')])


def bmi():
    height = input("Input your height(cm)：", type=FLOAT)
    weight = input("Input your weight(kg)：", type=FLOAT)

    BMI = weight / (height / 100) ** 2

    top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

    for top, status in top_status:
        if BMI <= top:
            put_markdown('# **Results**')
            put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
            put_html('<br><br>')
            put_markdown('Your BMI: `%.1f`. Category: `%s`' % (BMI, status))
            put_html('<hr>')
            put_table([
                ['Your BMI', 'Category'],
                [BMI, status],
            ])

            break


# Uncomment when running in local
# if __name__ == '__main__':
#     pywebio.start_server(welcome, port=7171)


# app.add_url_rule('/booking', 'webio_view', webio_view(welcome), methods=['GET', 'POST', 'OPTIONS'])


# app.run(host='localhost', port=80)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(welcome, port=args.port)









