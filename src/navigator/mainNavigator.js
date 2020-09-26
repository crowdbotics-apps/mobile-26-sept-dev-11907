import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import BlankScreen311240Navigator from '../features/BlankScreen311240/navigator';
import BlankScreen211239Navigator from '../features/BlankScreen211239/navigator';
import BlankScreen011236Navigator from '../features/BlankScreen011236/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
BlankScreen311240: { screen: BlankScreen311240Navigator },
BlankScreen211239: { screen: BlankScreen211239Navigator },
BlankScreen011236: { screen: BlankScreen011236Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
