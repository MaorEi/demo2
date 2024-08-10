module.exports = {
  apps: [
    {
      name: 'django',
      script: 'demoproject/demoproject/manage.py',
      args: 'runserver',
      instances: 1,
      autorestart: true,
      watch: false,
      max_memory_restart: '1G',
      env: {
        DJANGO_SETTINGS_MODULE: 'demoproject.settings',
        PYTHONUNBUFFERED: '1',
      },
    },
  ],
};