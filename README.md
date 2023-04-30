# v_logger Documentation

The `v_logger` is a Python module that provides a simple way to log messages to the console. It allows you to set a log type and prefix for your messages, and also includes predefined log types such as success, info, output, pending, debug, and error.

## Usage

To use `v_logger`, first import the module:

```python
from v_logger import logg
```

Then, create an instance of the `logg` class with a profile name and directory path:

```python
logger = logg('profile_name', 'log_directory')
```

Once you have an instance of the `logg` class, you can set the log type:

```python
logger.logg = 'info'
```

And log a message to the console:

```python
logger.lprint('This is an information message.')
```

## Configuration

The `v_logger` module includes a default configuration, but you can customize it by creating a configuration file using the `config` module included in the package. 

```python
from v_logger.configs import config

api_config = config()
api_config.add_config(config, 'profile_name', 'log_directory')
```

This will create a JSON configuration file in the specified directory with the specified profile name.

You can also customize the default log types by modifying the `logg_config` dictionary in the `logg` class.

## Predefined Log Types

The following predefined log types are available:

- `success`: A message indicating a successful operation
- `info`: An informational message
- `output`: A message that provides program output
- `pending`: A message indicating a pending operation
- `debug`: A message for debugging purposes
- `error`: A message indicating an error occurred

## Conclusion

The `v_logger` module provides a simple way to log messages to the console with customizable log types and configurations. It is an excellent tool for debugging and monitoring program output.
