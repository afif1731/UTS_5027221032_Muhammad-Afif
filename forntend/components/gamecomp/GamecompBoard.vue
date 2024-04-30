<template>
    <div class="container">
        <div class="row justify-content-center justify-content-lg-between h-100">
            <div class=" col-12 col-lg-7 m-3 order-1">
                <div class="game-board-up d-flex justify-content-center justify-content-lg-start container">
                    <div class="game-board d-flex flex-column p-3 rounded-5">
                        <div class="row">
                            <div class="mt-2 mb-4 col-12" v-if="curr_stat == 'PLAYING'">
                                <h3 style="color: #b5174f;" class="text-center" v-if="curr_turn === 'X'">{{ player2 }} TURN</h3>
                                <h3 style="color: #1762b5;" class="text-center" v-else>{{ player1 }} TURN</h3>
                            </div>
                            <div class="mt-2 mb-4 col-12" v-else>
                                <h3 style="color: #1762b5;" class="text-center" v-if="win_cell === def_p1">{{ win_msg }}</h3>
                                <h3 style="color: #b5174f;" class="text-center" v-else>{{ win_msg }}</h3>
                            </div>
                        </div>
                        <div class="row h-100 justify-content-center">
                            <div class="col-10 align-self-center px-lg-5">
                                <div class="w-100 h-auto d-flex position-relative">
                                    <img src="/icons/board.svg" class="board-img m-0">                       
                                    <div class="row position-absolute top-0 right-0 m-0 p-0 justify-content-between align-items-stretch w-100 h-100">
                                        <div class="col-4 board-cell-up"
                                            v-for="(cell, index) in curr_board"
                                            :key="index"
                                        >
                                            <div class="board-cell">
                                                <img v-if="index === curr_sel" src="/icons/piece_select.svg" class="m-0 position-absolute piece-select">

                                                <img v-if="cell === 'X'" src="/icons/red_player.svg" class="m-0 position-absolute pieces" @click="cellClicked(index)">
                                                <img v-else-if="cell === 'O'" src="/icons/blue_player.svg" class="m-0 position-absolute pieces" @click="cellClicked(index)">
                                                <img v-else src="/icons/red_player.svg" class="m-0 opacity-0 position-absolute pieces" @click="cellClicked(index)">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="w-100 d-none d-md-block"></div>
            
            <div class=" col-12 col-lg-4 m-3 order-2 mb-4 d-flex justify-content-center">
                <div class="card stat-card">
                    <h5 class="card-header text-center py-3">GAME STAT</h5>
                    <div class="card-body">
                        <h6 class="card-subtitle mt-3 mb-3 mb-lg-5 text-muted text-center">PLAYER 1 VS PLAYER 2</h6>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                        <div class="d-flex justify-content-between row px-3 mx-1 mx-sm-3 m-xl-3 align-items-center h-50">
                            <button class="btn btn-success btn-outline-secondary btn-sm stat-btn col-3 col-lg-12 col-xl-3 my-2" type="button" @click="rerestart()">Restart ⟳</button>
                            <button class="btn btn-primary btn-outline-secondary btn-sm stat-btn col-3 col-lg-12 col-xl-3 my-2" type="button" @click="surrender(1)">P1 🏳️</button>
                            <button class="btn btn-danger btn-outline-secondary btn-sm stat-btn col-3 col-lg-12 col-xl-3 my-2" type="button" @click="surrender(2)">P2 🏳️</button>
                        </div>
                    </div>
                    <div class="card-footer text-muted text-center">
                        Started at : 30/04/2024 11:00
                    </div>
                </div>
            </div>
        </div>  
    </div>
</template>

<script lang="ts">
import {type ILocalDataSave, gameStatus } from '~/assets/model/gamedata.model';
import { def_game } from '~/assets/model/game.default';
import { mainGame } from '~/assets/game_func/game.main';

export default {
    data() {
        return {
            curr_board: ['', ''],
            def_p1: '',
            curr_turn: '',
            curr_stat: gameStatus.play,
            curr_avail: [0, 0, 0],
            curr_sel: -1,
            player1: 'PLAYER 1',
            player2: 'PLAYER 2',
            win_cell: '_',
            win_msg: '',
            flag: 0
        }
    },
    props: {
        gameType: String,
    },
    methods: {
        setWin(winmsg: string) {
            this.curr_stat = gameStatus.win;
            this.win_msg = winmsg;
            this.flag = -1;
        },
        cellClicked(index: number) {
            if(this.flag) {
                if(this.curr_avail.includes(index)) {
                    // this available!
                    this.curr_avail = [] as number[];
                    this.curr_board = mainGame.movePiece(this.curr_turn, this.curr_board, this.curr_sel, index);
                    
                    this.win_cell = mainGame.winCheck(this.curr_board, this.curr_turn);
                    if(this.win_cell !== '_') {
                        const winmsg = this.win_cell === this.def_p1 ? 'PLAYER 1 WIN!!' : 'PLAYER 2 WIN!!';
                        this.setWin(winmsg);
                    }

                    this.curr_turn = this.curr_turn === 'O' ? 'X' : 'O';
                } else {
                    // this not! >:(
                }

                this.curr_sel = -1;
                this.flag = 0;
            }
            else if(this.flag === 0) {
                if(this.curr_board[index] === this.curr_turn) {
                    this.curr_sel = index;
                    this.curr_avail = [] as number[];
                    this.curr_avail = mainGame.getAllMove(index, this.curr_board);
                    this.flag = 1;
                }
            }
        },
        surrender(player: number) {
            if(this.flag !== -1) {
                if(player === 1) {
                    this.win_cell = this.def_p1 === 'X' ? 'O' : 'X';
                    this.setWin('PLAYER 2 WIN!!');
                }
                else if(player === 2) {
                    this.win_cell = this.def_p1;
                    this.setWin('PLAYER 1 WIN!!');
                }
            }
        },
        rerestart() {
            this.flag = 0;
            this.win_cell = '_';
            this.win_msg = '';
            this.curr_avail = [].concat([0, 0, 0] as never[]);
            this.curr_sel = -1;
            this.curr_board = [].concat(def_game.board as never[]);
            this.curr_turn = this.def_p1;
            this.curr_stat = gameStatus.play;
        }
    },
    async mounted() {
        this.curr_board = [];
        this.def_p1 = def_game.p1;

        if(this.gameType === 'LPVP') {
            const localData: string | null = localStorage.getItem('lpvpData');

            if(localData) {
                const localParsed: ILocalDataSave = JSON.parse(localData) as ILocalDataSave;

                this.curr_turn = localParsed.curr_p;
                this.curr_board = [...localParsed.curr_board];
            }
            else {
                this.curr_turn = def_game.p1;
                this.curr_board = [...def_game.board];
            }
        }
        else {
            this.curr_turn = def_game.p1;
            this.curr_board = [...def_game.board];
        }
    }
}
</script>


<style>
.game-board-up {
    width: auto;
    height: 86vh;
}
.game-board {
    background-color: rgba(108, 139, 192, 0.15);
}
.board-img {
    width: 100%;
    height: auto;
    padding: 7.66%;
}
.board-cell-up {
    padding: 0%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.board-cell {
    margin: 0%;
    height: auto;
    width: auto;
    display: flex;
    align-items: center;
    justify-content: center;
}
.pieces {
    width: 12%;
}
.piece-select {
    width: 16.3%;
}

.stat-card {
    width: 100%;
}
.stat-btn {
    color: white;
}

@media screen and (max-width: 992px) {
    .game-board-up {
        width: 90%;
        height: fit-content;
    }
}

@media screen and (max-width: 576px) {
    .game-board-up {
        width: 100%;
        height: fit-content;
    }   
}
</style>