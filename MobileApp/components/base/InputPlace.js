import React from "react";
import {Text, View, TextInput } from 'react-native';

const Inputplace = function ({text, secure, state, that}) {
  return (
    <View style = {{flexDirection:'row', marginTop: 15}}>
        <Text style = {{fontWeight:'bold', marginTop: 10, color:'rgba(58, 78, 207, 0.95)'}}>{text}</Text>
        <TextInput
            style={{height: 35, width: 280, borderRadius: 5, backgroundColor:'#d9d9d9',shadowColor: "#000000",shadowOpacity: 0.8,shadowRadius: 2,shadowOffset: {height: 1,width: 1}}}
            autoCapitalize='none'
            placeholder=""
            placeholderTextColor='black'
            textAlign = 'center'
            secureTextEntry = {secure}
            onChangeText={(input) => {
                    const set = {};
                    set[state] = input;
                    that.setState(set);
                    }}
        />
    </View>
  )
}
export default Inputplace;