
<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="primos"/>
        <attribute name="authors" value="CENTIC"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2024-08-22 08:45:31 a.&#160;m."/>
        <attribute name="created" value="Q0VOVElDO0hCMi01OzIwMjQtMDgtMjI7MDg6MzY6NTcgYS7CoG0uOzIzMTg="/>
        <attribute name="edited" value="Q0VOVElDO0hCMi01OzIwMjQtMDgtMjI7MDg6NDU6MzEgYS7CoG0uOzY7MjQyMw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n, i, divisores" type="Integer" array="False" size=""/>
            <declare name="divisible" type="Boolean" array="False" size=""/>
            <input variable="n"/>
            <assign variable="i" expression="2"/>
            <assign variable="divisible" expression="False"/>
            <while expression="i &lt; n &amp;&amp; divisible = False">
                <if expression="n % i == 0">
                    <then>
                        <assign variable="divisible" expression="True"/>
                    </then>
                    <else/>
                </if>
                <assign variable="i" expression="i + 1"/>
            </while>
            <if expression="divisible == True">
                <then>
                    <output expression="&quot;No es primo&quot;" newline="True"/>
                </then>
                <else>
                    <output expression="&quot;Es primo&quot;" newline="True"/>
                </else>
            </if>
            <output expression="i" newline="True"/>
        </body>
    </function>
</flowgorithm>