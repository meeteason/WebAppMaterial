import nebjs from 'nebulas'
const HttpRequest = nebjs.HttpRequest;
const Neb = nebjs.Neb;
const Account = nebjs.Account;
const Transaction = nebjs.Transaction;
const Unit = nebjs.Unit;
const Utils = nebjs.Utils
const myneb = new Neb();
myneb.setRequest(new HttpRequest("https://mainnet.nebulas.io"));
const nasApi = myneb.api;

export default{
    data(){
        return {}
    }
}