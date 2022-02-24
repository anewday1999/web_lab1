import * as React from 'react';
import Starts from './components/start'
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import Tutor from './components/tutor';
import Market from './components/market';
import Employee from './components/employee';
import tutorPost from './components/tutorPost'
import marketPost from './components/marketPost'
import employeePost from './components/employeePost'

const Stack = createStackNavigator();


export default class App extends React.Component {
  render(){
    return (
      <NavigationContainer>
        <Stack.Navigator>
          <Stack.Screen name="Starts" component={Starts} options={{
              headerShown: false,
            }}
          />
          <Stack.Screen name="Tutor" component={Tutor} options={{
              headerShown: false,
            }} 
          />
          <Stack.Screen name="Market" component={Market} options={{
              headerShown: false,
            }} 
          />
          <Stack.Screen name="Employee" component={Employee} options={{
              headerShown: false,
            }} 
          />
          <Stack.Screen name="tutorPost" component={tutorPost} options={{
              headerShown: false,
            }} 
          />
          <Stack.Screen name="marketPost" component={marketPost} options={{
              headerShown: false,
            }} 
          />
          <Stack.Screen name="employeePost" component={employeePost} options={{
              headerShown: false,
            }} 
          />
        </Stack.Navigator>
      </NavigationContainer>
    );
  }
  
}