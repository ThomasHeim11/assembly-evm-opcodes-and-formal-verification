object "HorseStoreYul"{
    code{
        datacopy(0,dataoffset("runtime"),datasize("runtime"))
        return(0,datasize("runtime"))
    }
    object "runtime"{
        code{
            switch selector()
            case 0xxcdfead2e{

            }
            case 0xe026c017{}

            default {
                revert(0,0)
            }
            function selector() -> s {
                s := div(calldataload(0), 0x100000000000000000000000000000000000000000000000000000000)
            }
        }
    }
}