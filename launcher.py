<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minecraft Launcher</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #1a2a6c, #b21f1f, #1a2a6c);
            color: white;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .launcher {
            background: rgba(0, 0, 0, 0.8);
            border-radius: 20px;
            padding: 30px;
            width: 90%;
            max-width: 400px;
            text-align: center;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
            border: 2px solid #3498db;
        }
        
        .logo {
            font-size: 3em;
            margin-bottom: 10px;
        }
        
        h1 {
            color: #e67e22;
            margin-bottom: 20px;
            font-size: 1.8em;
        }
        
        .version {
            background: #34495e;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 20px;
            font-size: 0.9em;
        }
        
        .btn {
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
            color: white;
        }
        
        .btn-java { background: linear-gradient(to right, #27ae60, #2ecc71); }
        .btn-bedrock { background: linear-gradient(to right, #3498db, #2980b9); }
        .btn-info { background: linear-gradient(to right, #f39c12, #e67e22); }
        .btn-exit { background: linear-gradient(to right, #e74c3c, #c0392b); }
        
        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }
        
        .status {
            margin-top: 20px;
            padding: 10px;
            border-radius: 10px;
            font-size: 0.9em;
            background: #34495e;
        }
        
        .tips {
            margin-top: 20px;
            font-size: 0.8em;
            color: #bdc3c7;
            line-height: 1.4;
        }
    </style>
</head>
<body>
    <div class="launcher">
        <div class="logo">🎮</div>
        <h1>MINECRAFT LAUNCHER</h1>
        
        <div class="version">
            Versión 2.0 - Multiplataforma
        </div>
        
        <button class="btn btn-java" onclick="launchJava()">
            ▶ Iniciar Java Edition
        </button>
        
        <button class="btn btn-bedrock" onclick="launchBedrock()">
            ▶ Iniciar Bedrock Edition
        </button>
        
        <button class="btn btn-info" onclick="showInfo()">
            ℹ️ Información
        </button>
        
        <button class="btn btn-exit" onclick="salir()">
            ❌ Salir
        </button>
        
        <div class="status" id="status">
            Listo para iniciar Minecraft
        </div>
        
        <div class="tips">
            💡 Consejo: Guarda esta página en favoritos<br>
            📱 Compatible con PC, móvil y tablet
        </div>
    </div>

    <script>
        // Función para actualizar el estado
        function updateStatus(text) {
            document.getElementById('status').innerText = text;
        }
        
        // Lanzar Minecraft Java
        function launchJava() {
            updateStatus("🚀 Iniciando Minecraft Java...");
            setTimeout(() => {
                alert("Minecraft Java se iniciaríá aquí\n(En PC: Abre el launcher oficial)");
                updateStatus("✅ Java Edition listo");
            }, 1000);
        }
        
        // Lanzar Minecraft Bedrock
        function launchBedrock() {
            updateStatus("🚀 Iniciando Minecraft Bedrock...");
            setTimeout(() => {
                alert("Minecraft Bedrock se iniciaríá aquí\n(En PC: Abre desde Microsoft Store)");
                updateStatus("✅ Bedrock Edition listo");
            }, 1000);
        }
        
        // Mostrar información
        function showInfo() {
            const info = `
🎮 MINECRAFT LAUNCHER 2.0

FUNCIONES:
• Iniciar Java Edition
• Iniciar Bedrock Edition
• Compatible multiplataforma
• Totalmente gratuito

DESARROLLADO PARA:
💻 PC - Ejecuta los launchers oficiales
📱 Móvil - Información y acceso rápido
🌐 Web - Acceso desde cualquier navegador

⚠️ NOTA: En dispositivos móviles solo muestra información. Para jugar, usa PC.
            `;
            alert(info);
            updateStatus("ℹ️ Información mostrada");
        }
        
        // Salir
        function salir() {
            if(confirm("¿Deseas salir del launcher?")) {
                updateStatus("👋 ¡Hasta pronto!");
                setTimeout(() => {
                    window.close();
                }, 1000);
            }
        }
        
        // Bienvenida
        window.onload = function() {
            updateStatus("👋 Bienvenido al Launcher");
        }
    </script>
</body>
</html>
