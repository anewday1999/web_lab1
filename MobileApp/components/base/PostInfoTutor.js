import React from "react";
import {Text, View } from 'react-native';
import styles from '../styles/mystyle.js';

export default function PostinfoTutor({title, main_content, subject, salary, contact, calendar}) {
  return (
    <View style={styles.board}>
        <Text style={styles.textInBtn}>{title}</Text>
        <Text style={styles.textInfo}>{main_content}</Text>
        <Text style={styles.textInfo}>Subject:      {subject}</Text>
        <Text style={styles.textInfo}>Salary:       {salary}</Text>
        <Text style={styles.textInfo}>Calendar:     {calendar}</Text>
        <Text style={styles.textInfo}>Contact:      {contact}</Text>
    </View>
  )
}

