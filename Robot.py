from mcpi import minecraft, block

class Robot:
    def __init__( self, mc, start_pos = minecraft.Vec3(0, 0, 0), start_dir = minecraft.Vec3(1, 0, 0) ):
        self.mc = mc
        
        self.pos = start_pos
        self.dir = start_dir

        self.start_pos = start_pos
        self.start_dir = start_dir

    def reset( self ):
        self.pos = self.start_pos
        self.dir = self.start_dir
        
    def render( self ):
        self.mc.setBlock( self.pos, block.STONE.id )
        self.mc.setBlock( self.pos + self.dir, block.TORCH.id )

    def forward( self ):
        self.pos = self.pos + self.dir

    def backward( self ):
        self.pos = self.pos - self.dir

    def left( self ):
        x, z = self.dir.x, self.dir.z
        self.dir.x = z
        self.dir.z = -x

    def right( self ):
        x, z = self.dir.x, self.dir.z
        self.dir.x = -z
        self.dir.z = x

mc = minecraft.Minecraft.create()
robot = Robot( mc )
robot.render()

