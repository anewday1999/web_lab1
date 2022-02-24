import React, { Component } from 'react';
import { Text, View } from 'react-native';
import styles from './styles/mystyle.js';
import Button from './base/Button'

export default class Starts extends Component {
  constructor(props){
    super(props)
  }
  tutor(){
    this.props.navigation.navigate('Tutor')
  }
  market(){
    this.props.navigation.navigate('Market')
  }
  employee(){
    this.props.navigation.navigate('Employee',)
  }
  render(){
    return (
      <View style={styles.container}>
        <Text style={{fontSize:40, fontWeight:'bold', color : '#000000', marginTop: 70, textAlign:'center'}}>Find your job!</Text>
        <Text style={{fontSize:40, fontWeight:'bold', color : '#000000', marginTop: 70, textAlign:'center'}}>And flea markets!</Text>
  
        <View style ={{marginTop:80}}></View>

        <Button text = 'Tutor' onPress = {() =>this.tutor()} />
  
        <View style ={{marginTop:35}}></View>
  
        <Button text = 'Market' onPress = {() =>this.market()} />

        <View style ={{marginTop:35}}></View>
  
        <Button text = 'Employee' onPress = {() =>this.employee()} />
  
      </View>
    );
  }
}
