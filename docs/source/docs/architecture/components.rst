Components
**********

.. _parser:

Parsers
=======

Parsers are :class:`reconfigure.parsers.BaseParser` subclasses which transform :ref:`raw config content <raw-config>` into :ref:`node trees <node-tree>` and vice versa

Making your own parser is as easy as subclassing :class:`reconfigure.parsers.BaseParser` and overriding ``parse`` and ``stringify`` methods.


.. _includer:

Includers
=========

Includers are used to handle the "include" directives in config files. Includers assemble the config file by finding the included files and parsing them and attaching them to the :ref:`node tree <node-tree>` of the main config. Reconfigure keeps track of which node belongs to which file by setting ``origin`` attribute on the included nodes

Example of includer in action:

    >>> from reconfigure.parsers import *
    >>> from reconfigure.includers import *
    >>> parser = IniFileParser()
    >>> includer = SupervisorIncluder(parser)
    >>> nodes = parser.parse(open('/etc/supervisor/supervisord.conf').read())
    >>> print nodes
    (None)
            (unix_http_server)
                    file = /var/run//supervisor.sock ((the path to the socket file))
                    chmod = 0700 (sockef file mode (default 0700))
            (supervisord)
                    logfile = /var/log/supervisor/supervisord.log ((main log file;default $CWD/supervisord.log))
                    pidfile = /var/run/supervisord.pid ((supervisord pidfile;default supervisord.pid))
                    childlogdir = /var/log/supervisor (('AUTO' child log dir, default $TEMP))
            (rpcinterface:supervisor)
                    supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
            (supervisorctl)
                    serverurl = unix:///var/run//supervisor.sock (use a unix:// URL  for a unix socket)
            (include)
                    files = /etc/supervisor/conf.d/*.conf

Note the "include" node in the end. Now we'll run an includer over this tree::

    >>> nodes = includer.compose('/etc/supervisor/supervisord.conf', nodes)
    >>> print nodes
    (None)
            (unix_http_server)
                    file = /var/run//supervisor.sock ((the path to the socket file))
                    chmod = 0700 (sockef file mode (default 0700))
            (supervisord)
                    logfile = /var/log/supervisor/supervisord.log ((main log file;default $CWD/supervisord.log))
                    pidfile = /var/run/supervisord.pid ((supervisord pidfile;default supervisord.pid))
                    childlogdir = /var/log/supervisor (('AUTO' child log dir, default $TEMP))
            (rpcinterface:supervisor)
                    supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
            (supervisorctl)
                    serverurl = unix:///var/run//supervisor.sock (use a unix:// URL  for a unix socket)
            <include> /etc/supervisor/conf.d/*.conf
            (program:test)
                    command = cat

Note how the include directive has turned into a junction point (:class:`reconfigure.nodes.IncludeNode`) and content of included files was parsed and attached.

Calling ``decompose`` method will split the tree back into separate files:

    >>> includer.decompose(nodes)
    {
        '/etc/supervisor/conf.d/1.conf': <reconfigure.nodes.RootNode object at 0x2c5cf10>, 
        '/etc/supervisor/supervisord.conf': <reconfigure.nodes.RootNode object at 0x2c5cb50>
    }

Writing your own includer
-------------------------

If you're up to writing a custom includer, take a look at :class:`reconfigure.includers.AutoIncluder`. It already implements the tree-walking and attachment logic, so you only need to implement two methods:

  * ``is_include(node)``: should check if the ``node`` is an include directive for this file format, and if it is, return a glob (wildcard) or path to the included files
  * ``remove_include(include_node)``: given an :class:`reconfigure.nodes.IncludeNode`, should transform it back into file-format-specific include directive and return it (as a :ref:`node tree <node-tree>` chunk)


.. _builder:

Builders
========

Builders transform :ref:`node trees <node-tree>` into :ref:`data trees <data-tree>`. 

To write your own builder, subclass :class:`reconfigure.builders.BaseBuilder` and override ``build`` and ``unbuild`` methods.