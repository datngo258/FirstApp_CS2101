import React from 'react';
import { createDrawerNavigator } from '@react-navigation/drawer';
import Home from '@/components/home/home';
import Login from '@/components/User/login';

const Drawer = createDrawerNavigator();

export default function DrawerNavigator() {
  return (
    <Drawer.Navigator initialRouteName="Home">  
      <Drawer.Screen name="Home" component={Home} />
      <Drawer.Screen name="Login" component={Login} />
    </Drawer.Navigator>
  );
}
