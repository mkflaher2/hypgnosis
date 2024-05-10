local font = lovr.graphics.getDefaultFont()
font:setPixelDensity(1)

local width, height = lovr.system.getWindowDimensions()
local projection = Mat4():orthographic(0, width, 0, height, -10, 10)

local spiralTexture = lovr.graphics.newTexture('images/spiral.jpg')
local spiralShader = lovr.graphics.newShader('unlit', 'unlit')

local viewCount = lovr.headset.getViewCount()
local currentView = 1

local function draw(pass)

    --local spiral = { x = width / 2, y = height / 2, w = width, h = height }

    local position = vec3(lovr.headset.getPosition('head'))
    local direction = vec3(lovr.headset.getDirection('head'))
    local orientation = quat(lovr.headset.getOrientation('head'))

    local radius = 5
    local length = 10

    local basePos = position - direction * 5

    local x, y, z = basePos:unpack()

    local scale = vec3(1,1,1)

    local dx, dy, dz = direction:unpack()

    local rotationMatrix = lovr.math.newMat4(basePos, scale, orientation)
    local composedMatrix = rotationMatrix:rotate(lovr.headset.getTime(), 0, 0, -1)
    local angle, ax, ay, az = composedMatrix:getOrientation()

    -- draw the cone
    pass:setColor(1,1,1)
    pass:setMaterial(spiralTexture)
    -- Pass:cone(position, scale, orientation, segments)
    --
    pass:cone(x, y, z, radius, length, angle, ax, ay, az)
    
    pass:setColor(1,0,0)
    pass:text(
        "angle: " .. string.format("%.2f", angle * 180 / math.pi) ..
        "; ax: " .. string.format("%.2f", ax) .. 
        "; ay: " .. string.format("%.2f", ay) ..  
        "; az: " .. string.format("%.2f", az),
        x, y, z + 1, 0.005, angle, ax, ay, az
    )

end

function lovr.draw(pass)
    draw(pass)
end
