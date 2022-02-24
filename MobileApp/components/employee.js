import React,  { Component } from 'react';
import { View, ScrollView, Text } from 'react-native';
import styles from './styles/mystyle.js';
import Button2 from './base/Button2'
import PostinfoEmployee from './base/PostInfoEmployee';
import axios from 'axios';

export default class Employee extends Component {
  constructor(props){
    super(props)
    this.state={
      fdata: []
    }
    
  }

  fetching() {
    axios.get('http://127.0.0.1/api/v1/employeePost')
      .then(res => {
        const fdata = res.data;
        this.setState({ fdata });
        console.log(this.state.fdata);
      })
  }
  componentDidMount() {
    const { navigation } = this.props;
    
    this.focusListener = navigation.addListener('focus', () => {
        // call your refresh method here
        this.fetching();
    });
  }

  componentWillUnmount() {
      // Remove the event listener
      if (this.focusListener != null && this.focusListener.remove) {
          this.focusListener.remove();
      }
  }
  post(){
    this.props.navigation.navigate('employeePost')
  }
  render(){
    const boards = []
    for (let i = 0; i < this.state.fdata.length; i++)
    {
      boards.push(<View key={i} style ={{marginTop:10}}></View>);
      boards.push(<PostinfoEmployee title = {this.state.fdata[i].title} main_content = {this.state.fdata[i].main_content} salary = {this.state.fdata[i].salary} contact = {this.state.fdata[i].contact} calendar = {this.state.fdata[i].calendar}/>);
    }
    return (
      <View style={styles.container}>

        <View style ={{marginTop:15}}></View>
        
        <Text style={{fontSize:40, fontWeight:'bold', color : '#000000', marginTop: 70, textAlign:'center'}}>Employee!</Text>

        <Button2 text = 'Post' onPress = {() =>this.post()} />

        <View style ={{marginTop:35}}></View>

        <ScrollView>

          {boards}
          
        </ScrollView>
      </View>
    );
  }
}
