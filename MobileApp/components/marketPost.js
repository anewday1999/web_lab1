import React,  { Component, useState } from 'react';
import { Text, View, TextInput } from 'react-native';
import styles from './styles/mystyle.js';
import Button from './base/Button';
import Inputplace from './base/InputPlace';
import axios from 'axios';

export default class marketPost extends Component {
  constructor(props){
    super(props)
    this.state={
      title: '',
      describe: '',
      address: '',
      price: '',
      contact: '',
    }
  }
  Submit(){
    
    console.log(typeof(this.state.title));
    console.log(this.state.describe);
    console.log(this.state.address);
    console.log(this.state.price);
    console.log(this.state.contact);
    // Simple POST request with a JSON body using axios
    const article = { title: this.state.title,
        describe: this.state.describe,
        address: this.state.address,
        price: this.state.price,
        contact: this.state.contact}

    axios({
        method: 'POST',
        url: 'http://127.0.0.1/api/v1/marketPost/',
        data: article,
        headers:{
          "Content-Type":"application/json",
          "accept": "application/json"
        }
    }).then(response => {
        console.log("response");
    });
    this.props.navigation.navigate('Market');

  
  }
  render(){
    
    return (
      <View className={styles.container}>
        <Text style={{fontSize:40, fontWeight:'bold', color : '#000000', marginTop: 70, textAlign:'center'}}>Post in market!</Text>

        <View style ={{marginTop:30}}></View>
        
        <View style = {{flexDirection:'row', marginTop: 15, marginLeft: 20}}>
          <Inputplace text='Title:                    ' secure={false} state='title' that={this}/>
        </View>

        <View style = {{flexDirection:'row', marginTop: 15, marginLeft: 20}}>
          <Inputplace text='Describe:           ' secure={false} state='describe' that={this}/>
        </View>

        <View style = {{flexDirection:'row', marginTop: 15, marginLeft: 20}}>
          <Inputplace text='Address:            ' secure={false} state='address' that={this}/>
        </View>

        <View style = {{flexDirection:'row', marginTop: 15, marginLeft: 20}}>
          <Inputplace text='Price:                  ' secure={false} state='price' that={this}/>
        </View>

        <View style = {{flexDirection:'row', marginTop: 15, marginLeft: 20}}>
          <Inputplace text='Contact:             ' secure={false} state='contact' that={this}/>
        </View>


        <View style ={{marginTop:80}}></View>

        <Button text = 'Submit' onPress = {() =>this.Submit()} />
  
        <View style ={{marginTop:35}}></View>
  
      </View>
    );
  }
}
