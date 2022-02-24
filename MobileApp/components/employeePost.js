import React,  { Component, useState } from 'react';
import { Text, View, TextInput } from 'react-native';
import styles from './styles/mystyle.js';
import Button from './base/Button';
import Inputplace from './base/InputPlace';
import axios from 'axios';

export default class employeePost extends Component {
  constructor(props){
    super(props)
    this.state={
      title: '',
      main_content: '',
      calendar: '',
      salary: '',
      contact: '',
    }
  }
  Submit(){
    
    console.log(typeof(this.state.title));
    console.log(this.state.main_content);
    console.log(this.state.salary);
    console.log(this.state.contact);
    console.log(this.state.calendar);
    // Simple POST request with a JSON body using axios
    const article = { title: this.state.title,
                      main_content: this.state.main_content,
                      salary: this.state.salary,
                      contact: this.state.contact,
                      calendar: this.state.calendar}
    axios({
        method: 'POST',
        url: 'http://127.0.0.1/api/v1/employeePost/',
        data: article,
        headers:{
          "Content-Type":"application/json",
          "accept": "application/json"
        }
    }).then(response => {
        console.log("response");
    });
    this.props.navigation.navigate('Employee');

  
  }
  render(){
    
    return (
      <View className={styles.container}>
        <Text style={{fontSize:40, fontWeight:'bold', color : '#000000', marginTop: 70, textAlign:'center'}}>Post in employee!</Text>

        <View style ={{marginTop:30}}></View>
        
        <View style = {{flexDirection:'row', marginTop: 15, marginLeft: 20}}>
          <Inputplace text='Title:                    ' secure={false} state='title' that={this}/>
        </View>

        <View style = {{flexDirection:'row', marginTop: 15, marginLeft: 20}}>
          <Inputplace text='Main_content:  ' secure={false} state='main_content' that={this}/>
        </View>

        <View style = {{flexDirection:'row', marginTop: 15, marginLeft: 20}}>
          <Inputplace text='Salary:                 ' secure={false} state='salary' that={this}/>
        </View>

        <View style = {{flexDirection:'row', marginTop: 15, marginLeft: 20}}>
          <Inputplace text='Contact:              ' secure={false} state='contact' that={this}/>
        </View>

        <View style = {{flexDirection:'row', marginTop: 15, marginLeft: 20}}>
          <Inputplace text='Calendar:            ' secure={false} state='calendar' that={this}/>
        </View>

        <View style ={{marginTop:80}}></View>

        <Button text = 'Submit' onPress = {() =>this.Submit()} />
  
        <View style ={{marginTop:35}}></View>
  
      </View>
    );
  }
}
