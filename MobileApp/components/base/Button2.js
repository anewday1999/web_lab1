import React from "react";
import {Text, TouchableOpacity } from 'react-native';
import styles from '../styles/mystyle.js';

export default function Button2({text, onPress}) {
  return (
    <TouchableOpacity onPress={onPress} style ={styles.button2}>
      <Text style={styles.textInBtn}>{text}</Text>
    </TouchableOpacity>
  )
}
