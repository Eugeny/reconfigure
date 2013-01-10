.. _reconfig:

Reconfig objects
****************

:class:`reconfigure.config.Reconfig` objects are pre-set pipelines connecting :ref:`Parsers <parser>`, :ref:`Includers <includer>` and :ref:`Builders <builder>`

Reconfigure comes with many Reconfig objects out-of-the-box - see :ref:`reconfigure.configs`

Writing your Reconfig subclass
==============================

Use the following pattern::

    class <name>Config (Reconfig):
        """
        <description>
        """

        def __init__(self, **kwargs):
            k = {
                'parser': <parser-class>(),
                'includer': <includer-class>(),
                'builder': BoundBuilder(<root-data-class>),
            }
            k.update(kwargs)
            Reconfig.__init__(self, **k)

Example::

    class SupervisorConfig (Reconfig):
        """
        ``/etc/supervisor/supervisord.conf``
        """

        def __init__(self, **kwargs):
            k = {
                'parser': IniFileParser(),
                'includer': SupervisorIncluder(),
                'builder': BoundBuilder(SupervisorData),
            }
            k.update(kwargs)
            Reconfig.__init__(self, **k)
