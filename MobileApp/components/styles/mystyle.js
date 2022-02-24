import { StyleSheet } from 'react-native';
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#C3D3D4',
    alignItems: 'center',
    justifyContent: 'flex-start',
  },
  button1:{
    alignSelf:'center',
    borderRadius: 10,
    backgroundColor: '#65E062',
    height: 50,
    width: 250,
  },
  button2:{
    alignSelf:'center',
    borderRadius: 10,
    backgroundColor: '#DF3712',
    height: 50,
    width: 250,
  },
  textInBtn:{
    fontSize : 20, 
    fontWeight:'bold', 
    color:'#000000', 
    marginTop:10, 
    textAlign:'center'},
  textInfo:{
    fontSize : 18, 
    color:'#000000', 
    marginTop:5, 
    marginLeft:10,
  },
  board:{
    width:410,
    height: 220,
    borderRadius: 15,
    backgroundColor: '#EDE3E3',
    borderColor:'#000000',
    borderWidth:2,
  }

});

export default styles;