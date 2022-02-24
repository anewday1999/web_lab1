import React from "react";
import {Text, TouchableOpacity } from 'react-native';
import styles from '../styles/mystyle.js';

export default function Button({text, onPress}) {
  return (
    <TouchableOpacity onPress={onPress} style ={styles.button1}>
      <Text style={styles.textInBtn}>{text}</Text>
    </TouchableOpacity>
  )
}
