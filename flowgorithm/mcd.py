
<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="mcd"/>
        <attribute name="authors" value="CENTIC"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-02-20 10:36:16 a.&#160;m."/>
        <attribute name="created" value="Q0VOVElDO0hCMi01OzIwMjUtMDItMjA7MTA6MzE6NTQgYS7CoG0uOzIyOTY="/>
        <attribute name="edited" value="Q0VOVElDO0hCMi01OzIwMjUtMDItMjA7MTA6MzY6MTYgYS7CoG0uOzE7MjQwNw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="mcd, i, n1, n2" type="Integer" array="False" size=""/>
            <input variable="n1"/>
            <input variable="n2"/>
            <if expression="n1 &lt; n2">
                <then>
                    <for variable="i" start="1" end="n1" direction="inc" step="1">
                        <if expression="n1 % i == 0 &amp;&amp; n2 % i == 0">
                            <then>
                                <assign variable="mcd" expression="i"/>
                            </then>
                            <else/>
                        </if>
                    </for>
                </then>
                <else>
                    <if expression="n1 &gt; n2">
                        <then>
                            <assign variable="i" expression="1"/>
                            <while expression="i &lt;= n2">
                                <if expression="n1 % i == 0 &amp;&amp; n2 % i == 0">
                                    <then>
                                        <assign variable="mcd" expression="i"/>
                                    </then>
                                    <else/>
                                </if>
                                <assign variable="i" expression="i + 1"/>
                            </while>
                        </then>
                        <else>
                            <assign variable="mcd" expression="n1"/>
                        </else>
                    </if>
                </else>
            </if>
            <output expression="mcd" newline="True"/>
        </body>
    </function>
</flowgorithm>