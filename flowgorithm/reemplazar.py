
<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="reemplazar"/>
        <attribute name="authors" value="CENTIC"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-02-20 12:20:11 p.&#160;m."/>
        <attribute name="created" value="Q0VOVElDO0hCMi01OzIwMjUtMDItMjA7MTE6NDU6MTMgYS7CoG0uOzIyOTc="/>
        <attribute name="edited" value="Q0VOVElDO0hCMi01OzIwMjUtMDItMjA7MTI6MjA6MTEgcC7CoG0uOzU7MjQxNg=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="entrada, salida, letra" type="String" array="False" size=""/>
            <declare name="n, i" type="Integer" array="False" size=""/>
            <input variable="entrada"/>
            <input variable="letra"/>
            <assign variable="n" expression="Len(entrada)"/>
            <assign variable="salida" expression="&quot;&quot;"/>
            <for variable="i" start="0" end="n - 1" direction="inc" step="1">
                <if expression="Char(entrada, i) == letra">
                    <then>
                        <assign variable="salida" expression="salida &amp; &quot;&quot;"/>
                    </then>
                    <else>
                        <if expression="Char(entrada, i) == &quot; &quot;">
                            <then>
                                <assign variable="salida" expression="salida &amp; &quot;,&quot;"/>
                            </then>
                            <else>
                                <assign variable="salida" expression="salida &amp; Char(entrada, i)"/>
                            </else>
                        </if>
                    </else>
                </if>
            </for>
            <output expression="salida" newline="True"/>
        </body>
    </function>
</flowgorithm>