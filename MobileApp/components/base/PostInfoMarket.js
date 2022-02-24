import React from "react";
import {Text, View } from 'react-native';
import styles from '../styles/mystyle.js';


export default function PostinfoMarket({title, describe, address, contact, price}) {
    return (
        <View style={styles.board}>
            <Text style={styles.textInBtn}>{title}</Text>
            <Text style={styles.textInfo}>{describe}</Text>
            <Text style={styles.textInfo}>Address:   {address}</Text>
            <Text style={styles.textInfo}>Contact:   {contact}</Text>
            <Text style={styles.textInfo}>Price:     {price}</Text>
        </View>
    )
}