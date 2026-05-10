import {
  BoxCubeIcon,
  GridIcon,
  ListIcon,
  LogoutIcon,
  PageIcon,
  SettingsIcon,
  UserCircleIcon,
} from '@/components/icons'

export const menuGroups = [
  {
    title: 'Menu',
    items: [
      {
        icon: GridIcon,
        label: 'Dashboard',
        name: 'dashboard',
      },
      {
        icon: PageIcon,
        label: 'Programs',
        name: null,
      },
      {
        icon: ListIcon,
        label: 'Workouts',
        name: null,
      },
      {
        icon: BoxCubeIcon,
        label: 'Exercises',
        name: 'exercises',
      },
    ],
  },
  {
    title: 'Account',
    items: [
      {
        icon: UserCircleIcon,
        label: 'Profile',
        name: null,
      },
      {
        icon: SettingsIcon,
        label: 'Settings',
        name: null,
      },
      {
        // Para logout no definimos ruta, lo maneja una acción
        icon: LogoutIcon,
        label: 'Logout',
        action: 'logout',
      },
    ],
  },
]
