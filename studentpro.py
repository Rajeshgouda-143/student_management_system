import streamlit as st
import sqlite3 as sq
conn=sq.connect('std.db')
curs=conn.cursor()
# table="""
# create table std(
# sid integer primary key AutoIncrement,
# sname text not null,
# age integer not null,
# phno integer unique not null check (length(phno)=10),
# email text unique not null,
# dob date not null,
# gender varchar(2) not null,
# address text not null,
# photo blob not null
# )
# """
# curs.execute(table)
# conn.commit()

def login():
    user_name=st.text_input('enter user name:')
    password=st.text_input('enter your password:',type='password')
    login=st.button('LOGIN',type='primary')
    if login:
        if user_name=='rajesh' and password=='Rajesh@123':
            st.session_state.is_logged=True
            st.success('login successful')
            st.rerun()
def add():
    name=st.text_input('enter your name:')
    age=st.number_input('enter your age:', min_value=0)
    phno=st.number_input('enter your phno:',min_value=0)
    email=st.text_input('enter your email:')
    dob=st.date_input('choose your dob:')
    gender=st.radio('choose your gender:',['male','female','other'])
    address=st.text_area('enter your address:')
    photo=st.file_uploader('upload your photo:',type=['jpg','png','svg','img'])
    insert=st.button('INSERT', type='primary')
    if insert:
        table="insert into std(sname,age,phno,email,dob,gender,address,photo) values (?,?,?,?,?,?,?,?)"
        photo_in_binary=photo.read()
        curs.execute(table, (name,age,phno,email,dob,gender,address,photo_in_binary))
        conn.commit()
        st.success('student  added.......')
        st.balloons()

def remove():
    sno=int(input('enter your sid:'))
    delete=st.button('DELETE',type='primary')
    if delete:
        table='delete from student where sid=?'
        curs.execute(table,(sno,))
        conn.commit()
        st.success('data removed successfully......')


def change_name():
    id=st.number_input('enter your sid:',min_value=0)
    new_name=st.text_input('enter your new_name:')
    upd=st.button('BUTTON',type='primary')
    if upd:
        table='update std set sname=? where sid=?'
        curs.execute(table,(new_name,id))
        conn.commit()
        st.success('update sname successfully.....')

def change_phno():
    id=st.number_input('enter your sid:',min_value=0)
    new_phno=st.number_input('enter your new_phno:',min_value=0)
    upd=st.button('BUTTON',type='primary')
    if upd:
        table='update std set phno=? where sid=?'
        curs.execute(table,(new_phno,id))
        conn.commit()
        st.success('update phno successfully......')

def change_age():
    id=st.number_input('enter your sid:',min_value=0)
    new_age=st.number_input('enter your new_age:',min_value=0)
    upd=st.button('BUTTON',type='primary')
    if upd:
        table='update std set age=? where sid=?'
        curs.execute(table,(new_age,id))
        conn.commit()
        st.success('update your age successfully....')

def change_email():
    id=st.number_input('enter your sid:',min_value=0)
    new_email=st.text_input('enter your new_email:')
    upd=st.button('BUTTON',type='primary')
    if upd:
        table='update std set email=? where sid=?'
        curs.execute(table,(new_email,id))
        conn.commit()
        st.success('update the email successfully......')

def change_dob():
    id=st.number_input('enter the sid:',min_value=0)
    new_dob=st.date_input('enter the new_dob:')
    upd=st.button('BUTTON',type='primary')
    if upd:
        table='update std set dob=? where sid=? '
        curs.execute(table,(new_dob,id))
        conn.commit()
        st.success('update your dob is successfully......')

def change_gender():
    id=st.number_input('enter your sid:',min_value=0)
    new_gender=st.text_input('enter your new_gender:',['male','female','other'])
    upd=st.button('BUTTON',type='primary')
    if upd:
        table='update std set gender=? where sid=?'
        curs.execute(table,(new_gender,id))
        conn.commit()
        st.success('your gender is update successfully...')

def change_address():
    id=st.number_input('enter your sid:',min_value=0)
    new_address=st.text_area('enter your new_address:')
    upd=st.button('BUTTON',type='primary')
    if upd:
        table='update std set address=? where sid=?'
        curs.execute(table,(new_address,id))
        conn.commit()
        st.success('update your address successfully.....')

def change_photo():
    id=st.number_input('enter your sid:',min_value=0)
    new_photo=st.file_uploader('upload your photo:',type=['jpg','png','svg','img'])
    upd=st.button('BUTTON',type='primary')
    if upd:
        table='update std set photo=? where sid=?'
        photo_chg=new_photo.read()
        curs.execute(table,(photo_chg,id))
        conn.commit()
        st.success('your photo upload successfully....')

def update():
    menu=['to change the sname','to change the age','to change the phno','to change the email','to update the dob','to change the gender','to change the address','to update the photo']
    op=st.selectbox('choose what you want to update:',menu)
    if op=='to change the sname':
        change_name()
    elif op=='to change the age':
        change_age()
    elif op=='to change the phno':
        change_phno()
    elif op=='to change the email':
        change_email()
    elif op=='to update the dob':
        change_dob()
    elif op=='to change the gender':
        change_gender()
    elif op=='to change the address':
        change_address()
    elif op=='to update the photo':
        change_photo()
def display():
    table="select * from std"
    data=curs.execute(table).fetchall()
    header=['SID','SNAME','AGE','PHNO','EMAIL','DOB','GENDER','ADDRESS','PHOTO']
    cols=st.columns(len(header))
    for column_name,column in zip(header,cols):
        column.markdown(column_name)
    for row in data:
        c1,c2,c3,c4,c5,c6,c7=st.columns(7)
        c1.write(row([0]))
        c1.write(row([1]))
        c1.write(row([2]))
        c1.write(row([3]))
        c1.write(row([4]))
        c1.write(row([5]))
        c1.write(row([6]))
        c1.write(row([7]))
        c1.image(row([8]))
#we are creating the variable called is_logged in the session state
if 'logged' not in st.session_state:
    st.session_state.is_logged=False
#if is_logged id true then if will be executed
if st.session_state.is_logged:
    menu=['add a student','display the student','remove the student','update the student']
    option=st.radio('choose the option:',menu)
    if option=='add a student':
       add()
    elif option=='display the student':
        display()
    elif option=='remove the student':
        remove()
    elif option=='update the student':
        update()
else:
    login()
