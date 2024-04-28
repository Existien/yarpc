/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/05.2_dictionaries_with_structs.yml
 *   Object: DictsWithStructs
 *   Template: qt6/service_source.j2
 */
#include "DictsWithStructsInterface.hpp"

using namespace gen::dicts;

DictsWithStructsInterface::DictsWithStructsInterface(QObject* parent)
: QObject(parent) {
    m_adaptor = new DictsWithStructsInterfaceAdaptor(this);
}

DictsWithStructsInterfaceAdaptor::DictsWithStructsInterfaceAdaptor(QObject* parent) : QDBusAbstractAdaptor(parent) {

}

void DictsWithStructsInterface::connect(){
    if (m_connection != nullptr) {
        return;
    }
    m_connection = std::make_unique<QDBusConnection>(QDBusConnection::connectToBus(QDBusConnection::SessionBus, "com.yarpc.testservice"));
    bool success = m_connection->isConnected();
    if (success) {
        success = success && m_connection->registerService("com.yarpc.testservice");
        success = success && m_connection->registerObject(
            "/com/yarpc/testservice",
            "com.yarpc.testservice.dictsWithStructs",
            this
        );
        if (!success) {
            m_connection->disconnectFromBus("com.yarpc.testservice");
        }
    }
    if (!success) {
        m_connection = nullptr;
    }
    emit connectedChanged();
}
void DictsWithStructsInterface::disconnect(){
    if (m_connection == nullptr) {
        return;
    }
    m_connection->disconnectFromBus("com.yarpc.testservice");
    m_connection = nullptr;
    emit connectedChanged();
}

bool DictsWithStructsInterface::getConnected() const {
    return m_connection != nullptr;
}

void DictsWithStructsInterfaceAdaptor::DictsStructMethod(const QDBusMessage &message){
    auto iface = dynamic_cast<DictsWithStructsInterface*>(parent());
    if (iface != nullptr) {
        message.setDelayedReply(true);
        iface->handleDictsStructMethodCalled(message);
    }
}

DictsStructMethodPendingReply::DictsStructMethodPendingReply(QDBusMessage call, QObject *parent) : QObject(parent) {
    m_call = call;
    m_args = DictsStructMethodArgs{};
}

DictsStructMethodArgs* DictsStructMethodPendingReply::args() {
    return &m_args;
}

void DictsStructMethodPendingReply::sendReply() {
    auto reply = m_call.createReply();
    auto iface = dynamic_cast<DictsWithStructsInterface*>(parent());
    if (iface != nullptr) {
        iface->callFinished(reply);
    }
    deleteLater();
}

void DictsStructMethodPendingReply::sendError(const QString& name, const QString& message) {
    auto error_reply = m_call.createErrorReply(name, message);
    auto iface = dynamic_cast<DictsWithStructsInterface*>(parent());
    if (iface != nullptr) {
        iface->callFinished(error_reply);
    }
    deleteLater();
}

void DictsStructMethodPendingReply::sendError(const DBusError &error) {
    auto error_reply = m_call.createErrorReply(error);
    auto iface = dynamic_cast<DictsWithStructsInterface*>(parent());
    if (iface != nullptr) {
        iface->callFinished(error_reply);
    }
    deleteLater();
}

void DictsWithStructsInterface::handleDictsStructMethodCalled(QDBusMessage call) {
    auto reply = new DictsStructMethodPendingReply(call, this);
    emit dictsStructMethodCalled(reply);
}
void DictsWithStructsInterface::EmitDictStructSignal(){
    emit m_adaptor->DictStructSignal();
}

void DictsWithStructsInterface::callFinished(const QDBusMessage &reply)
{
    m_connection->send(reply);
}