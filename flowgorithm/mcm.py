
<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="mcm"/>
        <attribute name="authors" value="CENTIC"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-02-20 11:09:31 a.&#160;m."/>
        <attribute name="created" value="Q0VOVElDO0hCMi01OzIwMjUtMDItMjA7MTE6MDY6MTIgYS7CoG0uOzIyOTM="/>
        <attribute name="edited" value="Q0VOVElDO0hCMi01OzIwMjUtMDItMjA7MTE6MDY6MTUgYS7CoG0uOzE7Q0VOVElDO0hCMi01OzIwMjUtMDItMjA7MTA6MzE6NTQgYS7CoG0uO21jZC5mcHJnOzU2MDM="/>
        <attribute name="edited" value="Q0VOVElDO0hCMi01OzIwMjUtMDItMjA7MTE6MDk6MzEgYS7CoG0uOzE7MjQwNQ=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="mcm, i, n1, n2" type="Integer" array="False" size=""/>
            <input variable="n1"/>
            <input variable="n2"/>
            <if expression="n1 &gt; n2">
                <then>
                    <for variable="i" start="n1 * n2" end="n1" direction="dec" step="1">
                        <if expression="i % n1 == 0 &amp;&amp; i % n2 == 0">
                            <then>
                                <assign variable="mcm" expression="i"/>
                            </then>
                            <else/>
                        </if>
                    </for>
                </then>
                <else>
                    <if expression="n1 &lt; n2">
                        <then>
                            <for variable="i" start="n1 * n2" end="n2" direction="dec" step="1">
                                <if expression="i % n1 == 0 &amp;&amp; i % n2 == 0">
                                    <then>
                                        <assign variable="mcm" expression="i"/>
                                    </then>
                                    <else/>
                                </if>
                            </for>
                        </then>
                        <else>
                            <assign variable="mcm" expression="n2"/>
                        </else>
                    </if>
                </else>
            </if>
            <output expression="mcm" newline="True"/>
        </body>
    </function>
</flowgorithm>